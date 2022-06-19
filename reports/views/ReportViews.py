import imp
from articles.serializers.ArticleConferenceDetail import ReportsrSerializer
from conferences.models import Conference
from reports.serializers.QuestionSerializer import QuestionSerializer
from reports.serializers.ReportSerializer import *
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination



class CreateReportView(generics.GenericAPIView):
    '''
    only reviewer can use this endpoint
    
    
    This endpoint is used to create a new report
    The user must be authenticated
    The questions must exist before submiting this
    A correct article must exist 
    if operation_success:
        status 201 + data
    if operation_failed:
        status 400, incorrect data
    '''
    serializer_class = ReportSerializer
    def post(self,request,format=None):
        try:
            sr = ReportSerializer(data=request.data,many=False)
            if sr.is_valid():
                    sr.validated_data['user']=request.user
                    sr.save()
                    return Response(sr.data,status=status.HTTP_201_CREATED)
            return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)   

class GetReportView(generics.GenericAPIView):
    serializer_class = ReportSerializer
    def get(self,request,id,format=None):
        '''
        only reviewer can use this endpoint
        
        
        this endpoint is used by reviewer to retrieve the report he hasnt done reviewing yet
        id = the id of the report he was doing 
        if he set review_done to true then he will recieve = "review for this article is done"
        else he will receive the old data he saved
        if report does not exist = status 404 report not found
        '''
        try:
            sr = ReportsrSerializer(Report.objects.get(pk=id))
            if not sr.data['review_done']:
                return Response(data=sr.data,status=status.HTTP_200_OK)
            return Response(data=sr.data,status=status.HTTP_200_OK)
        except:
            return Response("report not found",status=status.HTTP_404_NOT_FOUND)
    def put(self,request,id, format=None):
        '''
        only reviwer can use this endpoint
        
        
        this endpoint used by reviewer to update the report he hasnt finished (if review_done = False)
        id = the id of the report received from GET /report/report/id
        if report doesnt exist = status 404 + Report does not exist
        if the data is wrong or field missing = wrong data
        if request correct = new data + 200 OK
        '''
        try:
            rep = Report.objects.get(pk=id)
        except:
            return Response("Report does not exist",status=status.HTTP_404_NOT_FOUND)
        sr = ReportSerializer(rep,data=request.data)
        if sr.is_valid():
            sr.save()
            """
            if sr.validated_data["review_done"] :
            notification.objects.create(subject=str(user)+' had ' +serializer.validated_data["status"] + ' to review in conference  '+ str(conference),
            type='normal',invitation_status='pending',users=rep.article.conference_id.creator)"""
            return Response(sr.data,status=status.HTTP_200_OK)
        return Response("wrong data",status=status.HTTP_400_BAD_REQUEST)
class GetReportChairmanView(ModelViewSet):
    '''
    only chairman can use this endpoint
    
    
    this endpoint is used by the chairman to get the list of reports related to his conference
    '''
    serializer_class = ReportSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Report.objects.filter(article__conference_id__creator=self.request.user)
