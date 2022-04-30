from reports.models.ReportsModels import Question
from reports.serializers.QuestionSerializer import QuestionSerializer
from reports.serializers.ReportSerializer import *
from rest_framework import generics,status
from rest_framework.response import Response
from conferences.models import Conference



class AddQuestionView(generics.GenericAPIView): 
    '''
    only chairman can use this endpoint 
    
    
    this endpoint is used to add questions to confernces
    must provide id of the conference this question relates to
    '''
    serializer_class = QuestionSerializer   
    def post(self,request,format=None):
        try:
            assert Conference.objects.get(pk=request.data['conference'])
        except:
            return Response("Conference not found",status=status.HTTP_404_NOT_FOUND)
        sr = QuestionSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response("something went wrong",status=status.HTTP_404_NOT_FOUND)

class QuestionView(generics.GenericAPIView):
    serializer_class = QuestionSerializer
    def get(self,request,id,format=None):
        '''
        this endpoint is used to retrieve all the questions related to a conference
        id = the id of the conference
        '''
        try:
            qs = Question.objects.filter(conference=id)
        except:
            return Response("Conference does not exist",status=status.HTTP_404_NOT_FOUND)
        return Response(QuestionSerializer(qs,many=True).data,status=status.HTTP_200_OK)
    
    def put(self,request,id,format=None):
        '''
        only chairman can use this endpoint
        
        
        this endpoint is used to update a question, 
        id = id of the question 
        if the new data is incorrect = status 400+"incorrect date"
        if id incorrect = "question does not exist"
        else 200 OK + data
        '''
        try:
            qs = Question.objects.get(pk=id)
        except:
            return Response("Question does not exist",status=status.HTTP_404_NOT_FOUND)
        try:
            sr = QuestionSerializer(qs,data=request.data)
            if sr.is_valid():
                sr.save()
                return Response(sr.data,status=status.HTTP_200_OK)
            return Response("Incorrect data",status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Incorrect data",status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        '''
        only chairman can use this endpoint
        
        
        this endpoint is used to delete a question, 
        id = id of the question 
        if the new data is incorrect = status 400+"incorrect date"
        if id incorrect = "question does not exist"
        else 200 OK + data
        '''
        try:
            qs = Question.objects.get(pk=id)
        except:
            return Response("Question does not exist",status=status.HTTP_404_NOT_FOUND)
        try:
            sr = QuestionSerializer(qs,many=False)
            sr.delet()
            return Response("deleted !",status=status.HTTP_200_OK)
        except:
            return Response("Incorrect data",status=status.HTTP_400_BAD_REQUEST)
