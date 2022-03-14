import imp
from django.contrib import admin
from django.urls import path,include
from .views.RegisterView import RegisterView
from .views.LoginView import LoginView
from .views.UserView import UserView
from .views.LogoutView import LogoutView

urlpatterns = [
    
    #end point that return all the users exists
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserView.as_view()),
    path('logout',LogoutView.as_view())
]