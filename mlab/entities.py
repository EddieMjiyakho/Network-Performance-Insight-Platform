class Country:   # Represents a country with associated ISPs
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Region:   # Represents a region within a country
    def __init__(self, id, name, country_id):
        self.id = id
        self.name = name
        self.country_id = country_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_country_id(self):
        return self.country_id

    def set_name(self, name):
        self.name = name

    def set_country_id(self, country_id):
        self.country_id = country_id


class City:     # Represents a city within a region
    def __init__(self, id, name, region_id):
        self.id = id
        self.name = name
        self.region_id = region_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_region_id(self):
        return self.region_id

    def set_name(self, name):
        self.name = name

    def set_region_id(self, region_id):
        self.region_id = region_id


class ASN:      # Represents an Autonomous System Number
    def __init__(self, id, asn):
        self.id = id
        self.asn = asn

    def get_id(self):
        return self.id

    def get_asn(self):
        return self.asn

    def set_asn(self, asn):
        self.asn = asn


class AfricaRegion:   # Represents a region within Africa
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class NetworkPerformanceDataNormalized:    # Represents network performance metrics with normalized references
    def __init__(self, id, date, client_country_id, client_city_id, client_region_id, client_asn_id, avg_download_speed, avg_upload_speed, avg_latency, africa_region_id):
        self.id = id
        self.date = date
        self.client_country_id = client_country_id
        self.client_city_id = client_city_id
        self.client_region_id = client_region_id
        self.client_asn_id = client_asn_id
        self.avg_download_speed = avg_download_speed
        self.avg_upload_speed = avg_upload_speed
        self.avg_latency = avg_latency
        self.africa_region_id = africa_region_id

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_client_country_id(self):
        return self.client_country_id

    def get_client_city_id(self):
        return self.client_city_id

    def get_client_region_id(self):
        return self.client_region_id

    def get_client_asn_id(self):
        return self.client_asn_id

    def get_avg_download_speed(self):
        return self.avg_download_speed

    def get_avg_upload_speed(self):
        return self.avg_upload_speed

    def get_avg_latency(self):
        return self.avg_latency

    def get_africa_region_id(self):
        return self.africa_region_id

    def set_date(self, date):
        self.date = date

    def set_client_country_id(self, client_country_id):
        self.client_country_id = client_country_id

    def set_client_city_id(self, client_city_id):
        self.client_city_id = client_city_id

    def set_client_region_id(self, client_region_id):
        self.client_region_id = client_region_id

    def set_client_asn_id(self, client_asn_id):
        self.client_asn_id = client_asn_id

    def set_avg_download_speed(self, avg_download_speed):
        self.avg_download_speed = avg_download_speed

    def set_avg_upload_speed(self, avg_upload_speed):
        self.avg_upload_speed = avg_upload_speed

    def set_avg_latency(self, avg_latency):
        self.avg_latency = avg_latency

    def set_africa_region_id(self, africa_region_id):
        self.africa_region_id = africa_region_id
