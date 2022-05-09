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
    '''
    only admin account can use this endpoint

    
    with put methode can change the user is_active (True/False)
    True active
    False blocked
    if operation success status 200 
    if id is not valid status 400 body{'detail':invalid id}


    with delete methode 
    if operation success status 200 
    if id is not valid status 400 body{'detail':invalid id}
    '''
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
            return Response(data={'detail':'invalid id '},status=status.HTTP_400_BAD_REQUEST)
    #delete user (!!!!!!to continue!!!!!)
    def delete(self,request,id):
        #try:
            user=User.objects.get(id=id.replace('"',''))
            serializer=RegisterUserSerializer(user)
            serializer.data['is_active']=False
            user.delete() #delete user information (conferences articles) 
            User.objects.create(email=serializer.data['email'],password='hhhhh')
            return Response(status=status.HTTP_200_OK)
        #except:
            return Response(data={'detail':'invalid id '},status=status.HTTP_400_BAD_REQUEST)
