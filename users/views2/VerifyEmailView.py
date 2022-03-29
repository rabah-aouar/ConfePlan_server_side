from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

class VerifyEmailView(APIView):
    def post(self,request,id):
        user=User.objects.get(id=id)
        response = Response()
        if user is None:
            response.data= {
            'message': 'invalid id'
        }
        else:
            user.is_email_verified=True
            user.save()
            response.data = {
                'message': ' email verification successfully'
            }

        return response 