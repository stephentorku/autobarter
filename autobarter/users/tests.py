from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users.views import *

class TestUrls(SimpleTestCase):

    def test_login_view_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_chat_view_is_resolved(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func, registerPage)
    
    def test_logout_view_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logoutUser)