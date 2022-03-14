
from .views.LoginView import LoginView
from .views.UserView import UserView
from .views.LogoutView import LogoutView
from .views.RegisterView import RegisterView
from rest_framework.urls import path

urlpatterns = [
    
    #end point that return all the users exists
    path('login', LoginView.as_view()),
    path('profile', UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('register', RegisterView.as_view()),
]