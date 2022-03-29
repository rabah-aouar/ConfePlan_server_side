from ast import Delete
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework import status
from users.serializers.BlockUserSerializer import BlockUserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView

class AdminView(GenericAPIView):
    permission_class=[IsAdminUser]
    serializer_class=BlockUserSerializer
    #block user is_active=false
    #unblock user is_active=true
    def put(self, request ,id):
        serializer=BlockUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(id=id)
            user.is_active=serializer.data['is_active']
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            user=User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
