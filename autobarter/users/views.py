from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, 'users/login_page.html')

def registerPage(request):
    return render(request, 'users/register_page.html')