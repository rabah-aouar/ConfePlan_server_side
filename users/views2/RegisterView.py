from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        serializer= UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.errors
        serializer.save()
        return Response(serializer.data)


# Create your views here.
