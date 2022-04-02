from conferences.views.ConferenceView import ConferenceView
from conferences.views.ConferenceModificationView import ConferenceModificationView
from conferences.views.AdminView import AdminView
from conferences.views.ConferencesListView import ConferenceListView
from django.urls import path



urlpatterns = [
    path('<slug:id>', ConferenceModificationView.as_view()),
    path('',ConferenceView.as_view()),
    path('admin/<slug:id>',AdminView.as_view()),
    path('list/path',ConferenceListView.as_view({'get': 'list'}))
]
