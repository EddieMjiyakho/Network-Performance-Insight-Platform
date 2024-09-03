import pandas as pd
from django.core.management.base import BaseCommand
from mlab.models import NetworkPerformanceData, NetworkPerformanceDataNormalized, Country, City, Region, ASN, AfricaRegion
from django.db import transaction

class Command(BaseCommand):
    help = 'Normalize data from NetworkPerformanceData to NetworkPerformanceDataNormalized'

    def handle(self, *args, **kwargs):
        normalize_data()

def normalize_data():
    # Load data from the NetworkPerformanceData model into a DataFrame
    df = pd.DataFrame(list(NetworkPerformanceData.objects.all().values()))

    # Get unique values for each field
    unique_countries = df['clientCountry'].unique()
    unique_cities = df[['clientCity', 'clientCountry']].drop_duplicates()
    unique_regions = df[['clientRegion', 'clientCountry']].drop_duplicates()
    unique_asns = df['clientASN'].unique()
    unique_africa_regions = df['africa_regions'].unique()

    # Insert unique values into the new tables
    with transaction.atomic():
        # Insert countries
        country_objects = [Country(name=country) for country in unique_countries]
        Country.objects.bulk_create(country_objects, ignore_conflicts=True)

        # Insert cities
        city_objects = []
        for _, row in unique_cities.iterrows():
            country, _ = Country.objects.get_or_create(name=row['clientCountry'])
            city_objects.append(City(name=row['clientCity'], country=country))
        City.objects.bulk_create(city_objects, ignore_conflicts=True)

        # Insert regions
        region_objects = []
        for _, row in unique_regions.iterrows():
            country, _ = Country.objects.get_or_create(name=row['clientCountry'])
            region_objects.append(Region(name=row['clientRegion'], country=country))
        Region.objects.bulk_create(region_objects, ignore_conflicts=True)

        # Insert ASNs
        asn_objects = [ASN(asn=asn) for asn in unique_asns]
        ASN.objects.bulk_create(asn_objects, ignore_conflicts=True)

        # Insert Africa regions
        africa_region_objects = [AfricaRegion(name=africa_region) for africa_region in unique_africa_regions]
        AfricaRegion.objects.bulk_create(africa_region_objects, ignore_conflicts=True)

    # Create normalized data records
    with transaction.atomic():
        for record in NetworkPerformanceData.objects.all():
            # Retrieve or create normalized references
            country, _ = Country.objects.get_or_create(name=record.clientCountry)
            city, _ = City.objects.get_or_create(name=record.clientCity, country=country)
            region, _ = Region.objects.get_or_create(name=record.clientRegion, country=country)
            asn, _ = ASN.objects.get_or_create(asn=record.clientASN)
            africa_region, _ = AfricaRegion.objects.get_or_create(name=record.africa_regions)

            # Create new normalized data record
            NetworkPerformanceDataNormalized.objects.create(
                date=record.date,
                clientCountry=country,
                clientCity=city,
                clientRegion=region,
                clientASN=asn,
                avg_download_speed=record.avg_download_speed,
                avg_upload_speed=record.avg_upload_speed,
                avg_latency=record.avg_latency,
                africa_regions=africa_region
            )
