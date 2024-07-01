from django.urls import path

from .views import registration_form,student_register

urlpatterns = [
    path('', registration_form, name='registration_form'),
    path('register/', student_register, name='register'),
]
