from conferences.views.ConferenceView import ConferenceView
from conferences.views.ConferenceModificationView import ConferenceModificationView
from conferences.views.AdminView import AdminView

from django.urls import path



urlpatterns = [
    path('<slug:id>', ConferenceModificationView.as_view()),
    path('',ConferenceView.as_view()),
    path('admin',AdminView.as_view())
]
