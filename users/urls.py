
from ast import Delete

from users.views2.ProfileView import ProfileView
from users.views2.GetUserWithId import GetUserWithId
from users.views2.RegisterView import RegisterView
from users.views2.VerifyEmailView import VerifyEmailView
from users.views2.AdminView import AdminView
from users.views2.GetAllusersView import GetAllusersView
from users.views2.GetAllUsersForAdmin import GetAllUsersForAdmin
from django.urls import path



urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('<slug:id>',GetUserWithId.as_view()),
    path('register/', RegisterView.as_view()),
    path('verify-account/<str:id>', VerifyEmailView.as_view()),
    path('admin/<str:id>',AdminView.as_view()),
    path('list/path',GetAllusersView.as_view({'get': 'list'})),
    path('listforadmin/path',GetAllUsersForAdmin.as_view({'get': 'list'}))
]