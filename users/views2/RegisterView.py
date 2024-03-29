from rest_framework.generics import GenericAPIView
from users.serializers.UserProfileSerializer import RegisterUserSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from rest_framework import status


#function that send verification email
def send_verification_email(email,uuid):
    verification_page_link='http://127.0.0.1:8000/users/verify-account/'+uuid
    subject = 'confirm your account on Confeplan'
    message = 'Thanks for signing up with Confplan you must follow this link to activate your account\n'+verification_page_link
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return

class RegisterView(GenericAPIView):
    ''' end point for registration 
    if the registration end successfully response status 200  body : {{'id':----------,'message': 'confirmation email sent '
    if the registration failed status 400 body : {'email doesnt sent'} you have to verify the cnx (to send an email to the uset)
    '''
    permission_classes = ()  #allow any user to use this endpoint without authentification
    serializer_class=RegisterUserSerializer
    
    def post(self, request):
        serializer= RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.errors
        # save the user in db
        serializer.save()
        try :
            #try to send confirmation email 
            send_verification_email(serializer.data['email'],serializer.data['id'])
        except:
            #if the email doesnt send user will be deleted from the db
            User.objects.get(id=serializer.data['id']).delete()
            return Response(data={'email wasnt sent'},status=status.HTTP_400_BAD_REQUEST)

        response = Response()
        response.data = {
            'id':serializer.data['id'],
            'message': 'confirmation email sent ' 
        }
        
        return response


# Create your views here.
