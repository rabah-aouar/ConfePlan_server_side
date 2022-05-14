
from rest_framework import status
from conferences.models import Conference, DateType
from conferences.serializers.ConferenceDatesHistorySerializer import ConferenceDatesHistorySerializer
from ..serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from ..serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from ..serializers.ConferenceModificationSerializer import ConferenceModificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

class ConferenceModificationView(GenericAPIView):
    serializer_class=ConferenceModificationSerializer
    parser_classes = (FormParser, MultiPartParser)
    #get conference information with id of the conference 
    #if request from creator more information will be shown
    def get(self,request,id):
        try:
            conference=Conference.objects.get(id=id)
            print(conference)
            if conference.creator==request.user:
                return Response(data=ConferenceDetailForCreatorSerializer(conference).data,status=status.HTTP_200_OK)
            else:
                return Response(data=ConferenceDetailSerializer(conference).data,status=status.HTTP_200_OK)
        except:
            ##conference doesn't exist(wrong id)
            return Response(status=status.HTTP_404_NOT_FOUND)
    #change some information about conference allowed for craetor only
    def put(self,request,id):
        try:
            conference = Conference.objects.get(id=id)
            start_date=DateType.objects.get_or_create(type='start_date')
            start_date_id=start_date[0].id
            end_date=DateType.objects.get_or_create(type='end_date')
            end_date_id=end_date[0].id
            submition_deadline=DateType.objects.get_or_create(type='submition_deadline')
            submition_deadline_id=submition_deadline[0].id
            start_submition_date=DateType.objects.get_or_create(type='start_submition_date')
            start_submition_date_id=start_submition_date[0].id
            if conference.creator==request.user:
                serializer = ConferenceModificationSerializer(conference, data=request.data)
                if serializer.is_valid():
                    serializer.validated_data.pop('reviewers')
                    serializer.save()
                    if request.data.get('start_date') is not None:
                            sr1=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['start_date'],"type" :start_date_id,"conference":id})
                            sr1.is_valid(raise_exception=True)
                            sr1.save()
                    if request.data.get('end_date') is not None:
                            sr2=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['end_date'],"type" :end_date_id,"conference":id})
                            sr2.is_valid(raise_exception=True)
                            sr2.save()
                    if request.data.get('submition_deadline') is not None:
                            sr3=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['submition_deadline'],"type" :submition_deadline_id,"conference":id})
                            sr3.is_valid(raise_exception=True)
                            sr3.save()
                    if request.data.get('start_submition_date') is not None:
                            sr4=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['start_submition_date'],"type" :start_submition_date_id,"conference":id})
                            sr4.is_valid(raise_exception=True)
                            sr4.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        try:
            conference=Conference.objects.get(id=id)
            if conference.creator==request.user or request.user.is_admin:
                conference.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)