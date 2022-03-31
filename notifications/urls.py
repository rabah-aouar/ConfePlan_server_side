
from .NotificationView import NotificationView
from django.urls import path



urlpatterns = [
    path('', NotificationView.as_view()),
]