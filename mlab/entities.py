# @author: Maphuti Shilabje
# email: fabridgeshilabje01@gmail.com
# Date: 14/08/2024
# The class to store istances from the Database

# class User:   # This class represents a user in the system.
#     def __init__(self, id, username, email, password, role):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password = password
#         self.role = role

#     def get_id(self):
#         return self.id

#     def get_username(self):
#         return self.username

#     def get_email(self):
#         return self.email

#     def set_username(self, username):
#         self.username = username

#     def set_email(self, email):
#         self.email = email


class Country:   # This class represents a country, which has associated ISPs
    def __init__(self, id, country_name, ISPs):
        self.id = id
        self.country_name = country_name
        self.ISPs = ISPs

    def get_id(self):
        return self.id

    def get_country_name(self):
        return self.country_name

    def get_ISPs(self):
        return self.ISPs

    def set_country_name(self, country_name):
        self.country_name = country_name

    def set_ISPs(self, ISPs):
        self.ISPs = ISPs


class Region:   # This class represents a region within a country, also associated with ISPs.
    def __init__(self, id, region_name, ISPs):
        self.id = id
        self.region_name = region_name
        self.ISPs = ISPs

    def get_id(self):
        return self.id

    def get_region_name(self):
        return self.region_name

    def get_ISPs(self):
        return self.ISPs

    def set_region_name(self, region_name):
        self.region_name = region_name

    def set_ISPs(self, ISPs):
        self.ISPs = ISPs


class City:     # This class represents a region within a country, also associated with ISPs.
    def __init__(self, id, city_name, ISPs):
        self.id = id
        self.city_name = city_name
        self.ISPs = ISPs

    def get_id(self):
        return self.id

    def get_city_name(self):
        return self.city_name

    def get_ISPs(self):
        return self.ISPs

    def set_city_name(self, city_name):
        self.city_name = city_name

    def set_ISPs(self, ISPs):
        self.ISPs = ISPs


class NetworkMetric:    # This class represents network performance metrics collected for a specific location.
    def __init__(self, id, metric_name, value, timestamp, country_id, region_id, city_id):
        self.id = id
        self.metric_name = metric_name
        self.value = value
        self.timestamp = timestamp
        self.country_id = country_id
        self.region_id = region_id
        self.city_id = city_id

    def get_id(self):
        return self.id

    def get_metric_name(self):
        return self.metric_name

    def get_value(self):
        return self.value

    def get_timestamp(self):
        return self.timestamp

    def get_country_id(self):
        return self.country_id

    def get_region_id(self):
        return self.region_id

    def get_city_id(self):
        return self.city_id

    def set_metric_name(self, metric_name):
        self.metric_name = metric_name

    def set_value(self, value):
        self.value = value

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def set_country_id(self, country_id):
        self.country_id = country_id

    def set_region_id(self, region_id):
        self.region_id = region_id

    def set_city_id(self, city_id):
        self.city_id = city_id
