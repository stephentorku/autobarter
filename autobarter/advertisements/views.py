from turtle import title
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
import os

from .models import Advertisement, AdvertisementImage
# Create your views here.


def index(request):
    return render(request, 'advertisements/index.html')


def advertisements(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'advertisements/advertisements.html', context)

def details(request, id):
    advertisement = get_object_or_404(Advertisement, id=id)
    photos = AdvertisementImage.objects.filter(advertisement=advertisement)

    context ={'advertisement': advertisement, 'photos': photos}
    return render(request, 'advertisements/advertisement_details.html', context)

def load_model():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'autobarter_model.pkl')
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

@login_required(login_url='login')
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
        print(X)
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
            post_image = data['post_image'],
            description = data['description'],
            vendor = user,
            #calculate market value from model
            market_value = str(y_pred)
            )

        for image in images:
            photo = AdvertisementImage.objects.create(
            advertisement=advertisement,
            image=image,
        )




    return render(request, 'advertisements/new_advertisement.html')

@login_required(login_url="login")
def vendor_profile(request):
    return render(request, 'advertisements/vendor_profile.html')