from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', views.user_login, name='profile'),
    path('/login/', auth_views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
]