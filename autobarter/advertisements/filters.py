from django.forms import Select, TextInput, ChoiceField
import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter

from .models import *
import datetime

locations = (
        ('GA', 'Greater Accra'),
        ('VR', 'Volta Region'),
        ('ER', 'Eastern Region'),
        ('NR', 'Northern Region'),
        ('UE', 'Upper East Region'),
        ('UW', 'Upper West Region'),
        ('CR', 'Central Region'),
    )

transmissions = (
    ('a', 'Automatic'),
    ('m', 'Manual'),
)

car_models = (
        ('elantra', 'Elantra'),
        ('accent', 'Accent'),     
        ('accord', 'Accord'),
        ('civic', 'Civic'),
        ('rav4', 'Rav4'),
        ('corolla', 'Corolla'),
    )

car_makes = (
        ('hyundai', 'Hyundai'),
        ('toyota', 'Toyota'),     
        ('honda', 'Honda'),
    )


def year_choices():
        return [(r,r) for r in range(2005, datetime.date.today().year+1)]

class AdvertisementFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', widget=TextInput(attrs={'class':'custom-input-rect-filter', 'placeholder':'Title'}))
    minimum_price = django_filters.NumberFilter(field_name="selling_price", lookup_expr='gte', widget=TextInput(attrs={'class':'custom-input-rect-filter', 'placeholder':'Min. Price'}))
    maximum_price = django_filters.NumberFilter(field_name="selling_price", lookup_expr='lte', widget=TextInput(attrs={'class':'custom-input-rect-filter', 'placeholder':'Max. Price'}))
    make = ChoiceFilter(choices=car_makes, field_name="make", widget=Select(attrs={'class':'custom-input-rect-filter'}))
    model = ChoiceFilter(choices=car_models, field_name="model", widget=Select(attrs={'class':'custom-input-rect-filter'}))
    transmission = ChoiceFilter(choices=transmissions, field_name="transmission", widget=Select(attrs={'class':'custom-input-rect-filter'}))
    year_of_manufacture = ChoiceFilter(choices=year_choices(), field_name="year_of_manufacture", widget=Select(attrs={'class':'custom-input-rect-filter'}))
    location = ChoiceFilter(choices=locations, field_name="location", widget=Select(attrs={'class':'custom-input-rect-filter'}))

    class Meta:
        model = Advertisement
        fields = ['title', 'make', 'model', 'transmission', 'year_of_manufacture', 'location']

class AdvertisementHomeFilter(django_filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = ['location', 'make', 'model']