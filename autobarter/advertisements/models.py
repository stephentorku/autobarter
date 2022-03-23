from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Test(models.Model):
    title= models.CharField( max_length=50)

class Advertisement(models.Model):
    f_g = (
        ('f', 'Foreign Used'),
        ('g', 'Ghanaian Used'),
    )

    car_model = models.TextChoices('Car Model', 'elantra accent accord civic rav4 corolla')
    car_make = models.TextChoices('Car Make', 'hyundai honda toyota')
    body_types = models.TextChoices('Body Types', 'sedan suv hatchback')
    transmissions = (
        ('a', 'Automatic'),
        ('m', 'Manual'),
    )

    fuel_types = (
        ('p', 'Petrol'),
        ('d', 'Diesel'),
    )
    trim_edition_options = models.TextChoices('Trim/Edition', 'standard limited "full option" XLE GT sport touring SE LE EX')
    locations = (
        ('GA', 'Greater Accra'),
        ('VR', 'Volta Region'),
        ('ER', 'Eastern Region'),
        ('NR', 'Northern Region'),
        ('UE', 'Upper East Region'),
        ('UW', 'Upper West Region'),
        ('CR', 'Central Region'),
    )
    registered_choices = (
        ('y', 'Yes'),
        ('n', 'No'),
    )


    def year_choices():
        return [(r,r) for r in range(2005, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    title = models.CharField(max_length=100)
    foreign_ghana = models.CharField(max_length=1, choices=f_g)
    model = models.CharField(blank=True, choices=car_model.choices, max_length=10)
    make = models.CharField(blank=True, choices=car_make.choices, max_length=10)
    year_of_manufacture = models.IntegerField(choices=year_choices(), default=current_year())
    body_type = models.CharField(blank=True, choices=body_types.choices, max_length=10)
    mileage_km = models.IntegerField()
    transmission = models.CharField(max_length=1, choices=transmissions)
    fuel_type = models.CharField(max_length=1, choices=fuel_types)
    engine_capacity = models.DecimalField(max_digits=2, decimal_places=1)
    trim_edition = models.CharField(blank=True, choices=trim_edition_options.choices, max_length=15)
    location = models.CharField(max_length=2, choices=locations)
    car_registered = models.CharField(max_length=1, choices=registered_choices)
    registration_year = models.IntegerField(choices=year_choices(), default=current_year())
    market_value = models.CharField(max_length=50)
    description = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    



    
    


    
