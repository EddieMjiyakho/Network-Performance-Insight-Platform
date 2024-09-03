import pandas as pd
from django.core.management.base import BaseCommand
from mlab.models import NetworkPerformanceData, NetworkPerformanceDataNormalized, Country, City, Region, ASN, AfricaRegion
from django.db import transaction

class Command(BaseCommand):
    help = 'Normalize data from NetworkPerformanceData to NetworkPerformanceDataNormalized'

    def handle(self, *args, **kwargs):
        try:
            normalize_data()
            self.stdout.write(self.style.SUCCESS('Data normalization completed successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error during data normalization: {str(e)}'))

def normalize_data():
    # Load data from the NetworkPerformanceData model into a DataFrame
    df = pd.DataFrame(list(NetworkPerformanceData.objects.all().values()))

    # Get unique values for each field
    unique_countries = df['clientCountry'].unique()
    unique_cities = df[['clientCity', 'clientCountry']].drop_duplicates()
    unique_regions = df[['clientRegion', 'clientCountry']].drop_duplicates()
    unique_asns = df['clientASN'].unique()
    unique_africa_regions = df['africa_regions'].unique()

    # Insert unique values into the new tables and create normalized data records
    with transaction.atomic():
        # Insert countries
        for country in unique_countries:
            Country.objects.get_or_create(name=country)

        # Insert cities
        for _, row in unique_cities.iterrows():
            country, _ = Country.objects.get_or_create(name=row['clientCountry'])
            City.objects.get_or_create(name=row['clientCity'], country=country)

        # Insert regions
        for _, row in unique_regions.iterrows():
            country, _ = Country.objects.get_or_create(name=row['clientCountry'])
            Region.objects.get_or_create(name=row['clientRegion'], country=country)

        # Insert ASNs
        for asn in unique_asns:
            ASN.objects.get_or_create(asn=asn)

        # Insert Africa regions
        for africa_region in unique_africa_regions:
            AfricaRegion.objects.get_or_create(name=africa_region)

        # Create or update normalized data records
        for record in NetworkPerformanceData.objects.all():
            # Retrieve or create normalized references
            country, _ = Country.objects.get_or_create(name=record.clientCountry)
            city, _ = City.objects.get_or_create(name=record.clientCity, country=country)
            region, _ = Region.objects.get_or_create(name=record.clientRegion, country=country)
            asn, _ = ASN.objects.get_or_create(asn=record.clientASN)
            africa_region, _ = AfricaRegion.objects.get_or_create(name=record.africa_regions)

            # Create or update the normalized data record
            NetworkPerformanceDataNormalized.objects.update_or_create(
                date=record.date,
                clientCountry=country,
                clientCity=city,
                clientRegion=region,
                clientASN=asn,
                africa_regions=africa_region,
                defaults={
                    'avg_download_speed': record.avg_download_speed,
                    'avg_upload_speed': record.avg_upload_speed,
                    'avg_latency': record.avg_latency
                }
            )