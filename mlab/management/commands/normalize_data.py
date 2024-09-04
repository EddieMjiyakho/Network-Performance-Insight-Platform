from django.core.management.base import BaseCommand
from django.db import transaction
from mlab.models import (
    NetworkPerformanceData,
    ASN,
    AfricaRegion,
    Country,
    Region,
    City,
)

class Command(BaseCommand):
    help = 'Normalize data from NetworkPerformanceData model into separate tables'

    def handle(self, *args, **kwargs):
        self.normalize_data()

    def normalize_data(self):
        try:
            with transaction.atomic():
                # Fetch all records from NetworkPerformanceData
                network_data_records = NetworkPerformanceData.objects.all()

                # Extract unique values for each table
                unique_asns = set(record.clientASN for record in network_data_records)
                unique_africa_regions = set(record.africa_regions for record in network_data_records)
                unique_countries = set(record.clientCountry for record in network_data_records)
                unique_regions = set(record.clientRegion for record in network_data_records)
                unique_cities = set(record.clientCity for record in network_data_records)

                # Insert unique values into the new tables
                ASN.objects.bulk_create([ASN(asn=asn) for asn in unique_asns if asn], ignore_conflicts=True)
                AfricaRegion.objects.bulk_create([AfricaRegion(africa_region_name=name) for name in unique_africa_regions if name], ignore_conflicts=True)
                Country.objects.bulk_create([Country(country_name=name) for name in unique_countries if name], ignore_conflicts=True)
                Region.objects.bulk_create([Region(region_name=name) for name in unique_regions if name], ignore_conflicts=True)
                City.objects.bulk_create([City(city_name=name) for name in unique_cities if name], ignore_conflicts=True)

                self.stdout.write(self.style.SUCCESS("Data normalization completed successfully."))

        except Exception as e:
            # Catch any error that occurs during the normalization process
            self.stderr.write(f"Error during data normalization: {e}")




