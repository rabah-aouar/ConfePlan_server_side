from articles.views.ArticleView import ArticleView
from articles.views.EditArticle import EditArticle
from articles.views.UploadArticleView import UploadArticleView
from articles.views.AccepteToPublishView import AccepteToPublishView
from articles.views.ArticleListView import ArticleListView
from articles.views.RequestToEditView import RequestToEditView,GetRequestToEditView
from articles.views.ArticleListForSearcherView import ArticleListForSearcherView
from articles.views.ChangeArticleStatusForChairMan import ChangeArticleStatusForChairMan
from articles.views.WaitingForReviewArticle import WaitingForReviewArticle
from articles.views.AffectArticleToReviewer import AffectArticleToReviewer
from articles.views.removeReviewerfromArticleReviewersView import removeReviewerfromArticleReviewersView
from django.urls import path, re_path


urlpatterns = [
    path('',ArticleView.as_view()),
    path('upload_article/<slug:id>',UploadArticleView.as_view()),
    path('edit_article/<slug:id>',EditArticle.as_view()),
    path('edit_article/<slug:id>',EditArticle.as_view()),
    path('request_to_edit',RequestToEditView.as_view()),
    path('get/request_to_edit/<slug:request_to_edit_id>',GetRequestToEditView.as_view()),
    path('affect_article_to_reviewer',AffectArticleToReviewer.as_view()),
    path('remove_reviewer_from_article_reviewers',removeReviewerfromArticleReviewersView.as_view()),
    path('accepte_to_be_published/<slug:author_id>/<slug:article_id>',AccepteToPublishView.as_view()),
    path('list/path',ArticleListForSearcherView.as_view({'get': 'list'})),
    path('listforchairman/path/',ArticleListView.as_view({'get': 'list'})),
    path('listforreviewer/path',WaitingForReviewArticle.as_view({'get': 'list'})),
    path('<slug:id>',ChangeArticleStatusForChairMan.as_view())
]
