
from rest_framework import status
from users.serializers.UserProfileModificationSerializer import UserProfileModificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.models import User


class ProfileView(GenericAPIView):
    serializer_class=UserProfileModificationSerializer

    def get(self, request):
        if request.user.is_active:
            if request.user.is_email_verified:
                serializer = self.serializer_class(request.user)
                return Response(serializer.data)
            else:
                return Response({'message': 'email is not verified '},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'account is blocked'},status=status.HTTP_400_BAD_REQUEST)

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

