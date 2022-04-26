from articles.views.ArticleView import ArticleView
from articles.views.AccepteToPublishView import AccepteToPublishView
from django.urls import path



urlpatterns = [
    path('',ArticleView.as_view()),
    path('accepte_to_be_published/<slug:author_id>/<slug:article_id>',AccepteToPublishView.as_view())
]
