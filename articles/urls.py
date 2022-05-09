from articles.views.ArticleView import ArticleView
from articles.views.EditArticle import EditArticle
from articles.views.UploadArticleView import UploadArticleView
from articles.views.AccepteToPublishView import AccepteToPublishView
from articles.views.ArticleListView import ArticleListView
from articles.views.RequestToEditView import RequestToEditView
from articles.views.ChangeArticleStatusForChairMan import ChangeArticleStatusForChairMan
from django.urls import path



urlpatterns = [
    path('',ArticleView.as_view()),
    path('upload_article/<slug:id>',UploadArticleView.as_view()),
    path('edit_article/<slug:id>',EditArticle.as_view()),
    path('request_to_edit',RequestToEditView.as_view()),
    path('accepte_to_be_published/<slug:author_id>/<slug:article_id>',AccepteToPublishView.as_view()),
    path('list/path',ArticleListView.as_view({'get': 'list'})),
    path('<slug:id>',ChangeArticleStatusForChairMan.as_view()),
]
