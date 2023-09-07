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
]
