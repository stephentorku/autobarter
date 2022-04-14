from django.test import SimpleTestCase
from django.urls import resolve, reverse
from chat.views import *

class TestUrls(SimpleTestCase):

    def test_chat_page_is_resolved(self):
        url = reverse("chat", args=[1])
        self.assertEquals(resolve(url).func, chat)

    def test_check_chat_view_is_resolved(self):
        url = reverse("checkchat")
        self.assertEquals(resolve(url).func, checkChat)
    
    def test_send_chat_view_is_resolved(self):
        url = reverse("send")
        self.assertEquals(resolve(url).func, send)
    
    def test_get_messages_view_is_resolved(self):
        url = reverse("getMessages", args=[1])
        self.assertEquals(resolve(url).func, getMessages)
    
    def test_all_chats_view_is_resolved(self):
        url = reverse("all_chats")
        self.assertEquals(resolve(url).func, getChats)
