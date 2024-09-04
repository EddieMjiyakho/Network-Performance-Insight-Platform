from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.db.utils import DatabaseError

class Command(BaseCommand):
    help = 'Normalize data from NetworkPerformanceData into normalized tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            self.stdout.write('Starting update... Normalizing data into different schemas')

            try:
                with transaction.atomic():
                    # Insert ASN data
                    cursor.execute("""
                        INSERT INTO mlab_asn (asn)
                        SELECT DISTINCT "clientASN"
                        FROM mlab_networkperformancedata
                        WHERE "clientASN" IS NOT NULL
                        ON CONFLICT (asn) DO NOTHING
                    """)

                    # Insert AfricaRegion data with foreign key to ASN
                    cursor.execute("""
                        INSERT INTO mlab_africaregion (name, asn_id)
                        SELECT DISTINCT
                            npd."africa_regions",
                            asn.id
                        FROM mlab_networkperformancedata npd
                        JOIN mlab_asn asn
                            ON npd."clientASN" = asn.asn
                        WHERE npd."africa_regions" IS NOT NULL
                        ON CONFLICT (name) DO NOTHING
                    """)

                    # Insert Country data with foreign key to ASN
                    cursor.execute("""
                        INSERT INTO mlab_country (name, africa_region_id, asn_id)
                        SELECT DISTINCT
                            npd."clientCountry",
                            africa_region.id,
                            asn.id
                        FROM mlab_networkperformancedata npd
                        JOIN mlab_africaregion africa_region
                            ON npd."africa_regions" = africa_region.name
                        JOIN mlab_asn asn
                            ON npd."clientASN" = asn.asn
                        WHERE npd."clientCountry" IS NOT NULL
                        ON CONFLICT (name) DO NOTHING
                    """)

                    # Insert Region data with foreign key to ASN
                    cursor.execute("""
                        INSERT INTO mlab_region (name, country_id, asn_id)
                        SELECT DISTINCT
                            npd."clientRegion",
                            country.id,
                            asn.id
                        FROM mlab_networkperformancedata npd
                        JOIN mlab_country country
                            ON npd."clientCountry" = country.name
                        JOIN mlab_asn asn
                            ON npd."clientASN" = asn.asn
                        WHERE npd."clientRegion" IS NOT NULL
                        ON CONFLICT (name) DO NOTHING
                    """)

                    # Insert City data with foreign key to ASN
                    cursor.execute("""
                        INSERT INTO mlab_city (name, region_id, asn_id)
                        SELECT DISTINCT
                            npd."clientCity",
                            region.id,
                            asn.id
                        FROM mlab_networkperformancedata npd
                        JOIN mlab_region region
                            ON npd."clientRegion" = region.name
                        JOIN mlab_asn asn
                            ON npd."clientASN" = asn.asn
                        WHERE npd."clientCity" IS NOT NULL
                        ON CONFLICT (name) DO NOTHING
                    """)

                    # Insert NetworkMetric data with foreign key to ASN
                    cursor.execute("""
                        INSERT INTO mlab_networkmetric (avg_download_speed, avg_upload_speed, avg_latency, asn_id)
                        SELECT DISTINCT 
                            npd."avg_download_speed", 
                            npd."avg_upload_speed", 
                            npd."avg_latency", 
                            asn.id
                        FROM mlab_networkperformancedata npd
                        JOIN mlab_asn asn ON npd."clientASN" = asn.asn
                        WHERE npd."avg_download_speed" IS NOT NULL
                          AND npd."avg_upload_speed" IS NOT NULL
                          AND npd."avg_latency" IS NOT NULL
                          AND npd."clientASN" IS NOT NULL
                        ON CONFLICT (avg_download_speed, avg_upload_speed, avg_latency, asn_id) DO NOTHING
                    """)

                    self.stdout.write('Normalization complete.')

            except DatabaseError as e:
                self.stderr.write(f'Database error occurred: {e}')
            except Exception as e:
                self.stderr.write(f'Error occurred: {e}')



