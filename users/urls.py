
from users.views2.LoginView import LoginView
from users.views2.ProfileView import ProfileView
from users.views2.LogoutView import LogoutView
from users.views2.RegisterView import RegisterView
from django.urls import path

urlpatterns = [
    
    #end point that return all the users exists
    path('login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('logout',LogoutView.as_view()),
    path('register', RegisterView.as_view()),
]