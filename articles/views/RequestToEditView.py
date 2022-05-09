from rest_framework import status
from articles.models.Article import Article
from articles.serializers.RequestToEditSerializer import RequestToEditSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

class RequestToEditView(GenericAPIView):
    """end point to create the request to edit article
        if the request is created successfuly response status 201 body request object
        else status 400 body errors
    """
    serializer_class=RequestToEditSerializer
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
            serializer= RequestToEditSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['user']=request.user
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # save the creator in db
