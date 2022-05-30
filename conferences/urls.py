from http.client import ImproperConnectionState
from conferences.views.ConferenceReviewers import ConferenceReviewers
from conferences.views.ConferenceView import ConferenceView
from conferences.views.ConferenceModificationView import ConferenceModificationView
from conferences.views.AdminView import AdminView
from conferences.views.ConferencesListView import ConferenceListView
from conferences.views.ConferencesListForAdminView import ConferencesListForAdminView
from conferences.views.AccepteToReview import AccepteToReview
from conferences.views.ConferenceslistForCreator import ConferenceslistForCreator
from django.urls import path



urlpatterns = [
    path('<slug:id>', ConferenceModificationView.as_view()),
    path('',ConferenceView.as_view()),
    path('admin/<slug:id>',AdminView.as_view()),
    path('accepte_to_review/<slug:id>',AccepteToReview.as_view()),
    path('list/path',ConferenceListView.as_view({'get': 'list'})),
    path('reviewers/list/<slug:id>',ConferenceReviewers.as_view()),
    path('admin/list/path',ConferencesListForAdminView.as_view({'get': 'list'})),
    path('conferences_creator/list/path',ConferenceslistForCreator.as_view({'get': 'list'}))
]
