from conferences.models import Conference
from users.models import User
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework.filters import SearchFilter
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework import status

class ConferenceReviewers(GenericAPIView):
    permission_classes=()
    def post(self,request,id):
        try:
            conference=Conference.objects.get(id=id)
            reviewers=conference.reviewers.all()
            serializer=UserProfileModificationSerializer(reviewers,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            ##conference doesn't exist(wrong id)
            return Response(status=status.HTTP_404_NOT_FOUND)