from django.shortcuts import render
from rest_framework import status
from notifications.NotificationSerializer import NotificationSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
# Create your views here.
class NotificationView(GenericAPIView):
    serializer_class=NotificationSerializer
    def get(self, request):
        serializer=self.serializer_class(data=request.user.notification_set.all(),many=True)
        serializer.is_valid()
        return Response(serializer.data,status=status.HTTP_200_OK)
            