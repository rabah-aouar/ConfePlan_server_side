from django.urls import path
from reports.views.QuestionViews import AddQuestionView, QuestionView
from reports.views.ReportViews import *


urlpatterns = [
    path('question/<int:id>',QuestionView.as_view()),
    path('question/',AddQuestionView.as_view()),
    path('report/',CreateReportView.as_view()),
    path('report/<slug:id>',GetReportView.as_view()),
    path('list/reports',GetReportChairmanView.as_view({'get': 'list'})),

]