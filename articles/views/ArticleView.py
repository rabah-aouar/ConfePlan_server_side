from rest_framework import status
from articles.serializers.ArticleDetailSerializer import ArticleDetailSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

class ArticleView(GenericAPIView):
    serializer_class=ArticleDetailSerializer
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
            serializer= ArticleDetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['user_id']=request.user
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # save the creator in db
                        
