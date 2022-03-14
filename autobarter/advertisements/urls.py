from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('advertisements', views.advertisements, name='advertisements'),
    path('details', views.details, name="details"),
    path('profile', views.vendor_profile, name="vendor"),
]
