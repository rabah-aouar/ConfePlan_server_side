from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

class VerifyEmailView(APIView):
    permission_classes=()
    serializer_class=None
    def post(self,request,id):
        try:
            user=User.objects.get(id=id.replace('"',''))
            user.is_email_verified=True
            user.save()
            return Response({
                    'message': ' email verification successfully'
                },status=status.HTTP_200_OK)
        except:
            return Response({'message': 'invalid id'},status=status.HTTP_400_BAD_REQUEST)
