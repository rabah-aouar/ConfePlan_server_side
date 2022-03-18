
from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


class ProfileView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            #payload will containe decoded information email password and id 
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)    
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)