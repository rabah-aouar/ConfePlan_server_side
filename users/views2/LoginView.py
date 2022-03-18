from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


class LoginView(APIView):
    def post(self, request):
        try:
            email=request.data['email']
        except:
            raise AuthenticationFailed('email is required.')
        try:
            password=request.data['password']
        except:
            raise AuthenticationFailed('password is required.')
            
        user=User.objects.get(email=email)
        if user is None:
            raise AuthenticationFailed('User not found')

        #user=User.objects.filter(email=email,password=password).values().first()
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        user_inforamtions=User.objects.filter(email=email).values().first()
        payload ={
            "id":user_inforamtions['id'],
            "email": user_inforamtions['email'],
            "password":user_inforamtions['password'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iat": datetime.datetime.utcnow() 
                }


        token = jwt.encode(payload, 'secret', algorithm='HS256') #generation of token


        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True) #set the token in the cookie
        response.data = {
            'jwt': token
        }
        return response



# Create your views here.