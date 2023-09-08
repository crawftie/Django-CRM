from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('user_record/<int:pk>', views.user_record, name='user_record'),
    path('delete_user_record/<int:pk>', views.delete_user_record, name='delete_user_record'),
    path('add_user_record/', views.add_user_record, name='add_user_record'),
    path('update_user_record/<int:pk>', views.update_user_record, name='update_user_record'),
    path('list_hospitals/', views.list_hospitals, name='list_hospitals'),
    path('list_doctors/', views.list_doctors, name='list_doctors'),
    path('list_specialisms/', views.list_specialisms, name='list_specialisms'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_specialism/', views.add_specialism, name='add_specialism'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('record_doctor/<int:pk>', views.record_doctor, name='record_doctor'),
    path('record_hospital/<int:pk>', views.record_hospital, name='record_hospital'),
    path('record_specialism/<int:pk>', views.record_specialism, name='record_specialism'),
    path('list_doctors_by_hospital/<int:hospital_id>/', views.list_doctors_by_hospital, name='list_doctors_by_hospital'),
]
