
from rest_framework import status
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.models import User
from rest_framework.parsers import FormParser, MultiPartParser


class ProfileView(GenericAPIView):
    '''
    put methode modify user profile 
    '''
    serializer_class=UserProfileModificationSerializer
    parser_classes = (FormParser, MultiPartParser)
    #get user profile informations
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    #modify user profile informations
    def put(self,request):
        try:
            user = User.objects.get(id=request.user.id)
        except user.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileModificationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

