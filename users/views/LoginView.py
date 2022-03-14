
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


class LoginView(APIView):
    def post(self, request):
        email=request.data['email']
        password=request.data['password']
        user= User.objects.filter(email=email).values().first()
        print(user)
        if user is None:
            raise AuthenticationFailed('User not found')
        user1=User.objects.filter(email=email,password=password).first()
        print(user1)
        if user1 is None :
            raise AuthenticationFailed('Incorrect password')

        payload ={
            "email": user['email'],
            "password":user['password'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iat": datetime.datetime.utcnow() 
                }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response



# Create your views here.