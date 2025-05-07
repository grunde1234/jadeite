from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_courses, name='add_courses'),
    path('view/', views.view_courses, name='view_courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('update/<int:course_id>/', views.update_course, name='update_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]