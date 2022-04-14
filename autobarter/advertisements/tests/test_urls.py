from django.test import SimpleTestCase
from django.urls import resolve, reverse
from advertisements.views import *

class TestUrls(SimpleTestCase):

    def test_index_page_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, index)

    def test_advertisements_page_is_resolved(self):
        url = reverse("advertisements")
        self.assertEquals(resolve(url).func, advertisements)

    def test_advertisement_details_page_is_resolved(self):
        url = reverse("details", args=[1])
        self.assertEquals(resolve(url).func, details)

    def test_new_advertisement_page_is_resolved(self):
        url = reverse("new_ad")
        self.assertEquals(resolve(url).func, new_ad)

    def test_new_advertisement_na_page_is_resolved(self):
        url = reverse("new_ad_na")
        self.assertEquals(resolve(url).func, new_ad_na)
    
    def test_vendor_profile_page_is_resolved(self):
        url = reverse("profile", args=['test_username'])
        self.assertEquals(resolve(url).func, vendor_profile)

    def test_value_car_page_is_resolved(self):
        url = reverse("value_car")
        self.assertEquals(resolve(url).func, value_car)

    def test_show_car_value_page_is_resolved(self):
        url = reverse("show_car_value")
        self.assertEquals(resolve(url).func, show_car_value)

    def test_dashboard_page_is_resolved(self):
        url = reverse("dashboard")
        self.assertEquals(resolve(url).func, dashboard)

    
    


   

        