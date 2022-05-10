from users.models import User
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework.filters import SearchFilter

class GetAllUsersForAdmin(ModelViewSet):
    ''' get the list of users
    '''
    serializer_class = UserProfileModificationSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['first_name','family_name','email']

    def get_queryset(self):
        return User.objects.filter(is_admin=False,is_email_verified=True)