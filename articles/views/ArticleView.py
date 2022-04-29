from rest_framework import status
from articles.models.Article import Article
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

class ArticleView(GenericAPIView):
    """ end point to create an article object 
        response status 200 body object
        else status 400 body errors
    """
    serializer_class=ArticleDetailSerializer
    def post(self, request):
            serializer= ArticleDetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['user_id']=request.user
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


