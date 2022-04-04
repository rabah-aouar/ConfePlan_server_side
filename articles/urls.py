from articles.views.ArticleView import ArticleView
from django.urls import path



urlpatterns = [
    path('',ArticleView.as_view())
]
