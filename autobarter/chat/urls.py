from unicodedata import name
from django.urls import path
from . import views

# from django.conf import settings 
# from django.conf.urls.static import static 

urlpatterns = [
    path('chat/<int:id>', views.chat, name="chat"),
    path('checkchat', views.checkChat, name='checkchat'),
    path('send', views.send, name='send'),
    path('getMessages/<int:chat_id>/', views.getMessages, name='getMessages'),
    path('all_chats', views.getChats, name="all_chats"),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
