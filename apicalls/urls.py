from django.contrib import admin
from django.urls import path,include
from.views import students_list_or_create,students_get_or_update,login

urlpatterns = [
    path('students', students_list_or_create, name="students_list_or_create"),
    path('students/<int:pk>/', students_get_or_update, name="students_get_or_update"),
    path('login/',login)
]