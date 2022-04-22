from distutils.log import error
from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
import os
from django.urls import reverse

from .models import Advertisement, AdvertisementImage, Comment
from .decorators import authenticated_users_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .filters import AdvertisementFilter, AdvertisementHomeFilter
from users.models import UserDetails
from django.contrib.auth.models import User
from .forms import UserDetailsForm
# Create your views here.


def index(request):
    advertisements = Advertisement.objects.all()

    context = {'advertisements': advertisements}
    return render(request, 'advertisements/index.html', context)


def advertisements(request):
    advertisements = Advertisement.objects.all()

    adFilter = AdvertisementFilter(request.GET, queryset=advertisements)
    advertisements = adFilter.qs 

    context = {'advertisements': advertisements, 'adFilter': adFilter}
    return render(request, 'advertisements/advertisements.html', context)

def details(request, id):
    advertisement = get_object_or_404(Advertisement, id=id)
    photos = AdvertisementImage.objects.filter(advertisement=advertisement)
    comments = Comment.objects.filter(advertisement=advertisement)
    vendor_details = UserDetails.objects.filter(user=advertisement.vendor)

    if request.method == 'POST':
        data = request.POST
        comment_body= data['comment']
        comment = Comment.objects.create(advertisement=advertisement, author=request.user, body=comment_body)

    context ={'advertisement': advertisement, 'photos': photos, 'comments': comments, 'vendor_details': vendor_details }
    return render(request, 'advertisements/advertisement_details.html', context)

def load_model():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'autobarter_new.pkl')
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

model_data = load_model()

regressor = model_data["model"]
le_fg = model_data["le_fg"]
le_model = model_data["le_model"]
le_make = model_data["le_make"]
le_body_type = model_data["le_body_type"]
le_transmission = model_data["le_transmission"]
le_location = model_data["le_location"]
le_registered = model_data["le_registered"]
le_fuel_type = model_data["le_fuel_type"]
le_trim_edition = model_data["le_trim_edition"]
mileage = model_data["mileage"]
engine_capacity = model_data["engine_capacity"]
registration_year = model_data["registration_year"]
year_of_manufacture = model_data["year_of_manufacture"]
model_error = model_data["error"]

@authenticated_users_only
@allowed_users(allowed_roles=['vendor'])
def new_ad(request):
    user = request.user

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')


        X = np.array([[
                      data['foreign_ghana'],
                      data['model'], 
                      data['make'],
                      int(data['year_of_manufacture']),       
                      data['body_type'],
                      float(data['mileage']), 
                      data['transmission'],
                      data['fuel_type'],
                      float(data['engine_capacity']),
                      data['trim_edition'],
                      data['location'],
                      data['car_registered'],
                      int(data['year_of_registration'])
        ]])
       
        X[:, 0] = le_fg.transform(X[:,0])
        X[:, 1] = le_model.transform(X[:,1])
        X[:, 2] = le_make.transform(X[:,2])
        X[:, 4] = le_body_type.transform(X[:,4])

        X[:, 6] = le_transmission.transform(X[:,6])
        X[:, 7] = le_fuel_type.transform(X[:,7])

        X[:, 9] = le_trim_edition.transform(X[:,9])
        X[:, 10] = le_location.transform(X[:,10])
        X[:, 11] = le_registered.transform(X[:,11])
        X = X.astype(float)


        
        y_pred = regressor.predict(X)
        print(model_error)


        rounded_error = int(round(model_error, -3))
        #create lower bound figure
        lower_bound = int(y_pred[0]) - rounded_error
        #create upper bound figure
        upper_bound = int(y_pred[0]) + rounded_error
        #round them to thousand
        #convert to string
        price_range = str(lower_bound) + " - " + str(upper_bound)



        advertisement = Advertisement.objects.create(
            title = data['title'],
            foreign_ghana = data['foreign_ghana'],
            model = data['model'],
            make = data['make'],
            year_of_manufacture = data['year_of_manufacture'],
            body_type = data['body_type'],
            mileage_km = data['mileage'],
            transmission = data['transmission'],
            fuel_type = data['fuel_type'],
            engine_capacity = data['engine_capacity'],
            trim_edition = data['trim_edition'],
            location = data['location'],
            car_registered = data['car_registered'],
            registration_year = data['year_of_registration'],
            selling_price = data['selling_price'],
             post_image = images[0],
            description = data['description'],
            vendor = user,
            #calculate market value from model
            #market_value = str(y_pred[0])
            market_value = price_range
            )

        for image in images:
            photo = AdvertisementImage.objects.create(
            advertisement=advertisement,
            image=image
        )

        return redirect(reverse('details', kwargs={"id": advertisement.id}))




    return render(request, 'advertisements/new_advertisement.html')

def new_ad_na(request):
    user = request.user

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        advertisement = Advertisement.objects.create(
            title = data['title'],
            foreign_ghana = data['foreign_ghana'],
            model = data['model'],
            make = data['make'],
            year_of_manufacture = data['year_of_manufacture'],
            body_type = data['body_type'],
            mileage_km = data['mileage'],
            transmission = data['transmission'],
            fuel_type = data['fuel_type'],
            engine_capacity = data['engine_capacity'],
            trim_edition = data['trim_edition'],
            location = data['location'],
            car_registered = data['car_registered'],
            registration_year = data['year_of_registration'],
            selling_price = data['selling_price'],
            post_image = images[0],
            description = data['description'],
            vendor = user,
            market_value = "Not Available"
            )

        for image in images:
            photo = AdvertisementImage.objects.create(
            advertisement=advertisement,
            image=image
        )

        return redirect(reverse('details', kwargs={"id": advertisement.id}))
    return render(request, 'advertisements/new_advertisement_na.html')




def vendor_profile(request, username):
    vendor = get_object_or_404(User, username=username)
    advertisements = Advertisement.objects.filter(vendor=vendor)
    vendor_details = UserDetails.objects.filter(user=vendor)

    context={'advertisements': advertisements, 'vendor': vendor, 'vendor_details': vendor_details}
    return render(request, 'advertisements/vendor_profile.html', context)

def value_car(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')


        X = np.array([[
                      data['foreign_ghana'],
                      data['model'], 
                      data['make'],
                      int(data['year_of_manufacture']),       
                      data['body_type'],
                      float(data['mileage']), 
                      data['transmission'],
                      data['fuel_type'],
                      float(data['engine_capacity']),
                      data['trim_edition'],
                      data['location'],
                      data['car_registered'],
                      int(data['year_of_registration'])
        ]])
       
        X[:, 0] = le_fg.transform(X[:,0])
        X[:, 1] = le_model.transform(X[:,1])
        X[:, 2] = le_make.transform(X[:,2])
        X[:, 4] = le_body_type.transform(X[:,4])

        X[:, 6] = le_transmission.transform(X[:,6])
        X[:, 7] = le_fuel_type.transform(X[:,7])

        X[:, 9] = le_trim_edition.transform(X[:,9])
        X[:, 10] = le_location.transform(X[:,10])
        X[:, 11] = le_registered.transform(X[:,11])
        X = X.astype(float)


        
        y_pred = regressor.predict(X)
        print(model_error)


        rounded_error = int(round(model_error, -3))
        #create lower bound figure
        lower_bound = int(y_pred[0]) - rounded_error
        #create upper bound figure
        upper_bound = int(y_pred[0]) + rounded_error
        #round them to thousand
        #convert to string
        price_range = str(lower_bound) + " - " + str(upper_bound)
        request.session['car_name'] =   data['make'] + " " + data['model'] + " " + str(data['year_of_manufacture'])
        request.session['market_value']= price_range
        return redirect('show_car_value')
    return render(request, 'advertisements/value_car.html')

def show_car_value(request):
    context={'car_name': request.session['car_name'],'market_value': request.session['market_value'] }
    return render(request, 'advertisements/value_results.html', context)

def dashboard(request):
    user = request.user
    user_details = request.user.userdetails
    advertisements = Advertisement.objects.filter(vendor=user)
    number_of_ads = advertisements.count()
    form = UserDetailsForm(instance=user_details)

    if request.method == 'POST':
        data = request.POST
        form = UserDetailsForm(request.POST, request.FILES,instance=user_details)
        if form.is_valid():
            form.save()
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.username = data['username']
            user.save(update_fields=['first_name', 'last_name', 'email', 'username'])



    context = {'form': form, 'number_of_ads': number_of_ads, 'advertisements': advertisements}
    return render(request, 'advertisements/dashboard.html', context)
