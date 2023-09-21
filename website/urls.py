from django.urls import path
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    # Pages for user Logout, Login and Registration
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # Pages for Listing Records
    path('hospital_templates/list_hospitals/', views.list_hospitals, name='list_hospitals'),
    path('doctor_templates/list_doctors/', views.list_doctors, name='list_doctors'),
    path('specialism_templates/list_specialisms/', views.list_specialisms, name='list_specialisms'),
    # Page for listing Doctors by the Hospital they work within
    path('doctor_templates/list_doctors_by_hospital/<int:hospital_id>/', views.list_doctors_by_hospital, name='list_doctors_by_hospital'),
    # Pages for Adding Records
    path('hospital_templates/add_hospital/', views.add_hospital, name='add_hospital'),
    path('specialism_templates/add_specialism/', views.add_specialism, name='add_specialism'),
    path('doctor_templates/add_doctor/', views.add_doctor, name='add_doctor'),
    # Pages for Viewing individual Records
    path('doctor_templates/record_doctor/<int:pk>', views.record_doctor, name='record_doctor'),
    path('hospital_templates/record_hospital/<int:pk>', views.record_hospital, name='record_hospital'),
    path('specialism_templates/record_specialism/<int:pk>', views.record_specialism, name='record_specialism'),
    # Pages for Updating Individual Records
    path('specialism_templates/update_specialism/<int:pk>', views.update_specialism, name='update_specialism'),
    path('doctor_templates/update_doctor/<int:pk>', views.update_doctor, name='update_doctor'),
    path('hospital_templates/update_hospital/<int:pk>', views.update_hospital, name='update_hospital'),
    # Pages for Deleting Resources
    path('delete_hospital/<int:pk>', views.delete_hospital, name='delete_hospital'),
    path('delete_doctor/<int:pk>', views.delete_doctor, name='delete_doctor'),
    path('delete_specialism/<int:pk>', views.delete_specialism, name='delete_specialism'),
    #Admin Portal Functions
    path('admin_templates/list_users/', views.list_users, name='list_users'),
    path('admin_templates/add_user/', views.add_user, name='add_user'),
    path('admin_templates/record_user/<int:pk>', views.record_user, name='record_user'),
    path('admin_templates/update_user/<int:pk>', views.update_user, name='update_user'),
    path('admin_templates/admin_update_user_password/<int:pk>/', views.admin_update_user_password, name='admin_update_user_password'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    #User Password Reset
    path('update_user_password/<int:pk>', auth_views.PasswordChangeView.as_view(
        template_name='update_user_password.html',
        success_url=reverse_lazy('home')  # Redirect to the 'home' URL after password change
    ), name='update_user_password'),
]

handler404 = 'website.views.custom_404'
handler500 = 'website.views.custom_500'