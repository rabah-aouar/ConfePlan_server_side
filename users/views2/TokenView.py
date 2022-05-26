

from tokenize import TokenError
from jwt import InvalidTokenError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User


class MyTokenView(TokenObtainPairView):
    """
    if account doesn't exist or blocked :response status 401 body {"detail": "No active account found with the given credentials"}}
    if email is not verified :response status 401 body {"detail":"email is not verified"}
    if email and password are both true response status 200/body: {accesstoken}
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidTokenError(e.args[0])
        serializer.validated_data.pop('refresh', None)
        user=User.objects.get(email=request.data['email'])
        if user.is_email_verified:
            return Response(data={'id':user.id,'is_admin':user.is_admin ,'access':serializer.validated_data['access']}, status=status.HTTP_200_OK)
        else:
            return Response({"detail":"email is not verified"}, status=status.HTTP_401_UNAUTHORIZED)