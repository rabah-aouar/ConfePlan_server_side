
from ast import Delete

from users.views2.ProfileView import ProfileView
#from users.views2.LogoutView import LogoutView
from users.views2.RegisterView import RegisterView
from users.views2.VerifyEmailView import VerifyEmailView
from users.views2.AdminView import AdminView
from django.urls import path



urlpatterns = [

    path('profile', ProfileView.as_view()),
    #path('logout',LogoutView.as_view()),
    path('register', RegisterView.as_view()),
    path('verify-account/<str:id>', VerifyEmailView.as_view()),
    path('admin/<str:id>',AdminView.as_view())
]