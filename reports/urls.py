from django.urls import path
from reports.views.views import ReportView

urlpatterns = [
    path('',ReportView.as_view())
]