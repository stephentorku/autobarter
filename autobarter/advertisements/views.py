from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


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

@login_required(login_url="login")
def vendor_profile(request):
    return render(request, 'advertisements/vendor_profile.html')