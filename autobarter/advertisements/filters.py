import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class AdvertisementFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    minimum_price = django_filters.NumberFilter(field_name="selling_price", lookup_expr='gte')
    maximum_price = django_filters.NumberFilter(field_name="selling_price", lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ['title', 'make', 'model', 'transmission', 'year_of_manufacture', 'location']

class AdvertisementHomeFilter(django_filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = ['location', 'make', 'model']