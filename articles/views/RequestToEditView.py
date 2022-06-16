from rest_framework import status
from articles.models.Article import Article
from articles.models.RequestToEdit import RequestToEdit
from articles.serializers.RequestToEditSerializer import RequestToEditSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser

from notifications.models import notification

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
                a=serializer.save()
                print(a)
                notification.objects.create(subject= "one of reviewers assk you to edit article of title "+str(serializer.validated_data['article'].title)+" before "+str(serializer.validated_data['deadline']),
                type='request_to_edit',request_to_edit_article_id=a.id,invitation_status="pending",users=serializer.validated_data['article'].user_id)
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # save the creator in db
class GetRequestToEditView(GenericAPIView):
    """end point to get the request to edit article
    """
    serializer_class=()
    #parser_classes = (FormParser, MultiPartParser)
    def get(self, request, request_to_edit_id):
        #try:
            req=RequestToEdit.objects.get(id=request_to_edit_id)
            return Response(data=RequestToEditSerializer(req).data,status=status.HTTP_200_OK)
        #except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            # save the creator in db

