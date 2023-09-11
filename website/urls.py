from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    # Pages for user Logout, Login and Registration
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # Pages for Listing Records
    path('list_hospitals/', views.list_hospitals, name='list_hospitals'),
    path('list_doctors/', views.list_doctors, name='list_doctors'),
    path('list_specialisms/', views.list_specialisms, name='list_specialisms'),
    # Page for listing Doctors by the Hospital they work within
    path('list_doctors_by_hospital/<int:hospital_id>/', views.list_doctors_by_hospital, name='list_doctors_by_hospital'),
    # Pages for Adding Records
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_specialism/', views.add_specialism, name='add_specialism'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    # Pages for Viewing individual Records
    path('record_doctor/<int:pk>', views.record_doctor, name='record_doctor'),
    path('record_hospital/<int:pk>', views.record_hospital, name='record_hospital'),
    path('record_specialism/<int:pk>', views.record_specialism, name='record_specialism'),
    # Pages for Updating Individual Records
    path('update_specialism/<int:pk>', views.update_specialism, name='update_specialism'),
    path('update_doctor/<int:pk>', views.update_doctor, name='update_doctor'),
    path('update_hospital/<int:pk>', views.update_hospital, name='update_hospital'),
    # Pages for Deleting Resources
    path('delete_hospital/<int:pk>', views.delete_hospital, name='delete_hospital'),
    path('delete_doctor/<int:pk>', views.delete_doctor, name='delete_doctor'),
    path('delete_specialism/<int:pk>', views.delete_specialism, name='delete_specialism'),
]
