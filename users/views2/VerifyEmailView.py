from django.http import HttpResponseRedirect
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

class VerifyEmailView(APIView):
    '''
    endpoint to email verification
    if operation success status 200  body:{'detail': ' email verification successfully'}
    if id is not valid status 400 body{'detail':invalid id}
    '''
    permission_classes=()
    serializer_class=None
    def get(self,request,id):
        try:
            user=User.objects.get(id=id.replace('"',''))
            user.is_email_verified=True
            user.save()
            return HttpResponseRedirect(redirect_to='http://127.0.0.1:3000/confirm')
        except:
            return Response({'message': 'invalid id'},status=status.HTTP_400_BAD_REQUEST)
