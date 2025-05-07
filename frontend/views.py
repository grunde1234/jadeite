from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as django_logout  # rename the imported logout



# Create your views here.
def index(request):
    company = 'Jadeite Tech Hub'
    slogan = 'Computer Training and Business Center'
    return render(request, 'frontend/index.html', {'company': company, 'slogan': slogan})

def services(request):
    return render(request, 'frontend/services.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # or 'home' or 'dashboard'
    else:
        form = UserCreationForm()
    return render(request, 'frontend/signup.html', {'form': form})

def dashboard(request):
    company = 'Jadeite Tech Hub'
    slogan = 'Computer Training and Business Center'
    return render(request, 'frontend/dashboard.html', {'company': company, 'slogan': slogan})

def logout_view(request):  # Renamed to avoid conflict
    django_logout(request)
    return redirect('login')  # Change 'login' to whatever route name you want to redirect t

