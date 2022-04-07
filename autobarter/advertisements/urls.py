from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name="home"),
    path('advertisements/', views.advertisements, name='advertisements'),
    path('details/<int:id>/', views.details, name='details'),
    path('profile/<str:username>', views.vendor_profile, name='profile'),
    path('new_ad/', views.new_ad, name='new_ad'),
    path('new_ad_na', views.new_ad_na, name='new_ad_na'),
    path('value_car', views.value_car, name='value_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
