from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'advertisements/index.html')


def advertisements(request):
    return render(request, 'advertisements/advertisements.html')

def details(request):
    return render(request, 'advertisements/advertisement_details.html')

@login_required(login_url="login")
def vendor_profile(request):
    return render(request, 'advertisements/vendor_profile.html')