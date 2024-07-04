from django.urls import path

from .views import registration_form, student_register, student_list, mark_as_paid, export_students_to_excel

urlpatterns = [
    path('', registration_form, name='registration_form'),
    path('register/', student_register, name='register'),
    path('students/', student_list, name='student_list'),
    path('mark_as_paid/<int:id>/', mark_as_paid, name='mark_as_paid'),
    path('student_report/', export_students_to_excel, name="student_report")
]
