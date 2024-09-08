class Country:
    # Represents a country with associated ISPs
    def __init__(self, id, country_name):
        self.id = id
        self.country_name = country_name

    def get_id(self):
        return self.id

    def get_country_name(self):
        return self.country_name

    def set_country_name(self, country_name):
        self.country_name = country_name


class Region:
    # Represents a region within a country
    def __init__(self, id, region_name):
        self.id = id
        self.region_name = region_name

    def get_id(self):
        return self.id

    def get_region_name(self):
        return self.region_name

    def set_region_name(self, region_name):
        self.region_name = region_name


class City:
    # Represents a city within a region
    def __init__(self, id, city_name):
        self.id = id
        self.city_name = city_name

    def get_id(self):
        return self.id

    def get_city_name(self):
        return self.city_name

    def set_city_name(self, city_name):
        self.city_name = city_name


class ASN:
    # Represents an Autonomous System Number
    def __init__(self, id, asn):
        self.id = id
        self.asn = asn

    def get_id(self):
        return self.id

    def get_asn(self):
        return self.asn

    def set_asn(self, asn):
        self.asn = asn


class AfricaRegion:
    # Represents a region within Africa
    def __init__(self, id, africa_region_name):
        self.id = id
        self.africa_region_name = africa_region_name

    def get_id(self):
        return self.id

    def get_africa_region_name(self):
        return self.africa_region_name

    def set_africa_region_name(self, africa_region_name):
        self.africa_region_name = africa_region_name


class NetworkPerformanceData:
    # Represents network performance metrics with references to other models
    def __init__(self, id, date, client_country, client_city, client_region, client_asn, avg_download_speed, avg_upload_speed, avg_latency, africa_regions):
        self.id = id
        self.date = date
        self.client_country = client_country
        self.client_city = client_city
        self.client_region = client_region
        self.client_asn = client_asn
        self.avg_download_speed = avg_download_speed
        self.avg_upload_speed = avg_upload_speed
        self.avg_latency = avg_latency
        self.africa_regions = africa_regions

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_client_country(self):
        return self.client_country

    def get_client_city(self):
        return self.client_city

    def get_client_region(self):
        return self.client_region

    def get_client_asn(self):
        return self.client_asn

    def get_avg_download_speed(self):
        return self.avg_download_speed

    def get_avg_upload_speed(self):
        return self.avg_upload_speed

    def get_avg_latency(self):
        return self.avg_latency

    def get_africa_regions(self):
        return self.africa_regions

    def set_date(self, date):
        self.date = date

    def set_client_country(self, client_country):
        self.client_country = client_country

    def set_client_city(self, client_city):
        self.client_city = client_city

    def set_client_region(self, client_region):
        self.client_region = client_region

    def set_client_asn(self, client_asn):
        self.client_asn = client_asn

    def set_avg_download_speed(self, avg_download_speed):
        self.avg_download_speed = avg_download_speed

    def set_avg_upload_speed(self, avg_upload_speed):
        self.avg_upload_speed = avg_upload_speed

    def set_avg_latency(self, avg_latency):
        self.avg_latency = avg_latency

    def set_africa_regions(self, africa_regions):
        self.africa_regions = africa_regions
