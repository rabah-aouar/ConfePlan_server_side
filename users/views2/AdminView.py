from ast import Delete
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework import status
from users.serializers.BlockUserSerializer import BlockUserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView

from users.serializers.UserProfileSerializer import RegisterUserSerializer

class AdminView(GenericAPIView):
    permission_classes=[IsAdminUser] #only admins can use this end point
    serializer_class=BlockUserSerializer
    #block user is_active=false
    #unblock user is_active=true
    def put(self, request ,id):
        serializer=BlockUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(id=id.replace('"',''))
            user.is_active=serializer.data['is_active']
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #delete user (!!!!!!to continue!!!!!)
    def delete(self,request,id):
        try:
            user=User.objects.get(id=id.replace('"',''))
            serializer=RegisterUserSerializer(user)
            serializer.data['is_active']=False
            user.delete() #delete user information (conferences articles) 
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
