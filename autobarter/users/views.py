from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username OR Password is incorrect")

        context={}
        return render(request, 'users/login_page.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                account_type=request.POST.get('user_type')
                group = Group.objects.get(name=str(account_type))
                user.groups.add(group)
                messages.success(request, "Account successfully created")
                return redirect('login')

        context = {'form': form}
        return render(request, 'users/register_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')