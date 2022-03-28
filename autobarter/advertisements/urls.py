from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name="home"),
    path('advertisements', views.advertisements, name='advertisements'),
    path('details/<int:id>/', views.details, name="details"),
    path('profile', views.vendor_profile, name="vendor"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
