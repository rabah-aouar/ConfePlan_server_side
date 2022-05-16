
from rest_framework import status
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.models import User
from rest_framework.parsers import FormParser, MultiPartParser


class GetUserWithId(GenericAPIView):
    '''
    '''
    serializer_class=UserProfileModificationSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes=()
    #get user profile informations
    def get(self, request,id):
        try:
            user=User.objects.get(id=id)
            serializer = self.serializer_class(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
