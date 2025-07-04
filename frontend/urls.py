from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/',views.services, name='services'),
    path('signup/',  views.signup, name='signup'),
    path('dashboard/',  views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]

