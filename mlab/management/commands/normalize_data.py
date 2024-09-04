from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Normalize data from NetworkPerformanceData into normalized tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            self.stdout.write('Starting update...Normalise data to different schemas')
            
            try:
                # Insert ASN data
                cursor.execute("""
                    INSERT INTO mlab_asn (asn)
                    SELECT DISTINCT "clientASN"
                    FROM mlab_networkperformancedata
                    WHERE "clientASN" IS NOT NULL
                    ON CONFLICT (asn) DO NOTHING;
                """)

                # Insert NetworkMetric data
                cursor.execute("""
                    INSERT INTO mlab_networkmetric (asn_id, avg_download_speed, avg_upload_speed, avg_latency)
                    SELECT a.id, npd.avg_download_speed, npd.avg_upload_speed, npd.avg_latency
                    FROM mlab_networkperformancedata npd
                    JOIN mlab_asn a ON a.asn = npd."clientASN"
                    ON CONFLICT (asn_id, avg_download_speed, avg_upload_speed, avg_latency) DO NOTHING;
                """)

                # Insert AfricaRegion data
                cursor.execute("""
                    INSERT INTO mlab_africaregion (name)
                    SELECT DISTINCT "africa_regions"
                    FROM mlab_networkperformancedata
                    WHERE "africa_regions" IS NOT NULL
                    ON CONFLICT (name) DO NOTHING;
                """)

                # Insert Country data
                cursor.execute("""
                    INSERT INTO mlab_country (name, africa_region_id, network_metric_id)
                    SELECT DISTINCT npd."clientCountry", ar.id, nm.id
                    FROM mlab_networkperformancedata npd
                    JOIN mlab_africaregion ar ON ar.name = npd."africa_regions"
                    JOIN mlab_networkmetric nm ON nm.asn_id = (SELECT id FROM mlab_asn WHERE asn = npd."clientASN")
                    ON CONFLICT (name, africa_region_id, network_metric_id) DO NOTHING;
                """)

                # Insert Region data
                cursor.execute("""
                    INSERT INTO mlab_region (name, country_id, africa_region_id, network_metric_id)
                    SELECT DISTINCT npd."clientRegion", c.id, ar.id, nm.id
                    FROM mlab_networkperformancedata npd
                    JOIN mlab_country c ON c.name = npd."clientCountry"
                    JOIN mlab_africaregion ar ON ar.name = npd."africa_regions"
                    JOIN mlab_networkmetric nm ON nm.asn_id = (SELECT id FROM mlab_asn WHERE asn = npd."clientASN")
                    ON CONFLICT (name, country_id, africa_region_id, network_metric_id) DO NOTHING;
                """)

                # Insert City data
                cursor.execute("""
                    INSERT INTO mlab_city (name, client_region_id, country_id, africa_region_id, network_metric_id)
                    SELECT DISTINCT npd."clientCity", r.id, c.id, ar.id, nm.id
                    FROM mlab_networkperformancedata npd
                    JOIN mlab_region r ON r.name = npd."clientRegion"
                    JOIN mlab_country c ON c.name = npd."clientCountry"
                    JOIN mlab_africaregion ar ON ar.name = npd."africa_regions"
                    JOIN mlab_networkmetric nm ON nm.asn_id = (SELECT id FROM mlab_asn WHERE asn = npd."clientASN")
                    ON CONFLICT (name, client_region_id, country_id, africa_region_id, network_metric_id) DO NOTHING;
                """)

                self.stdout.write('Normalisation complete.')

            except Exception as e:
                self.stderr.write(f'Error occurred: {e}')

