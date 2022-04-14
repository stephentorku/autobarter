# from urllib import response
# from django.test import TestCase, Client
# from django.urls import reverse
# from advertisements.models import *
# from django.contrib.auth.models import User, Group
# import json

# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.vendor = User.objects.create(
#             first_name = "testvendorfirst",
#             last_name = "testvendorlast",
#             username = "testvendorusername",
#             email = "testvendor@gmail.com",
#             password = "testpass@123",
#         )
#         self.vendor.groups.add("vendor")    
#         self.buyer = User.objects.create(
#             first_name = "testbuyerfirst",
#             last_name = "testbuyerlast",
#             username = "testbuyerusername",
#             email = "testbuyer@gmail.com",
#             password = "testpass@123",
#         )    
#         self.buyer.groups.add("buyer") 
#         # self.advertisement = Advertisement.objects.create(
#         #     title = "test_ad",
#         #     foreign_ghana = "f",
#         #     model = "elantra",
#         #     make = "hyundai",
#         #     year_of_manufacture = "2015",
#         #     body_type = "sedan",
#         #     mileage_km = 5576,
#         #     transmission = 'a',
#         #     fuel_type = 'p',
#         #     engine_capacity = 1.8,
#         #     trim_edition = 'standard',
#         #     location = 'GA',
#         #     car_registered = 'y',
#         #     registration_year = '2018',
#         #     selling_price = 2000,
#         #     post_image = None,
#         #     description = "Test description",
#         #     vendor = self.vendor,
#         #     market_value = "Price range"
#         #     )    
    

#     def test_advertisements_page_GET(self):
#         response = self.client.get(reverse("advertisements"))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'advertisements/advertisements.html')

#     def test_new_advertisement_POST(self):
#         Advertisement.objects.create(
#             title = "test_ad",
#             foreign_ghana = "f",
#             model = "elantra",
#             make = "hyundai",
#             year_of_manufacture = "2015",
#             body_type = "sedan",
#             mileage_km = 5576,
#             transmission = 'a',
#             fuel_type = 'p',
#             engine_capacity = 1.8,
#             trim_edition = 'standard',
#             location = 'GA',
#             car_registered = 'y',
#             registration_year = '2018',
#             selling_price = 2000,
#             post_image = None,
#             description = "Test description",
#             vendor = self.vendor,
#             market_value = "Price range"
#             )
#         url = reverse("new_ad")

#         response = self.client.post(url, {
#             'title': "test_ad",
#             'foreign_ghana': "f",
#             'model': "elantra",
#             'make' : "hyundai",
#             'year_of_manufacture' : "2015",
#             'body_type' : "sedan",
#             'mileage_km' : '5576',
#             'transmission' : 'a',
#             'fuel_type' : 'p',
#             'engine_capacity' : 1.8,
#             'trim_edition' : 'standard',
#             'location' : 'GA',
#             'car_registered' : 'y',
#             'registration_year' : '2018',
#             'selling_price' : 2000,
#             'post_image' : None,
#             'description' : "Test description",
#             'vendor' : self.vendor,
#             'market_value' : "Price range"
#         })

#         self.assertEquals(response.status_code, 302)
