
from rest_framework import status
from conferences.models import Conference, ConferenceDatesHistory, ConferenceStatus, ConferneceStatusHistory, DateType
from conferences.serializers.ConferenceDatesHistorySerializer import ConferenceDatesHistorySerializer
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from conferences.serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from conferences.serializers.ConferenceStatusHistorySerializer import ConferenceStatusHistorySerializer
from notifications.models import notification

class ConferenceView(GenericAPIView):
    serializer_class=ConferenceDetailSerializer
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
            serializer= ConferenceDetailSerializer(data=request.data)
            start_date=DateType.objects.get_or_create(type='start_date')
            start_date_id=start_date[0].id
            end_date=DateType.objects.get_or_create(type='end_date')
            end_date_id=end_date[0].id
            submition_deadline=DateType.objects.get_or_create(type='submition_deadline')
            submition_deadline_id=submition_deadline[0].id
            start_submition_date=DateType.objects.get_or_create(type='start_submition_date')
            start_submition_date_id=start_submition_date[0].id
            pending=ConferenceStatus.objects.get_or_create(status='pending')
            pending_id=pending[0].id
            
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['creator']=request.user
                serializer.save()
                sr1=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['start_date'],"type" :start_date_id,"conference":serializer.data['id']})
                sr1.is_valid(raise_exception=True)
                sr1.save()
                sr2=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['end_date'],"type" :end_date_id,"conference":serializer.data['id']})
                sr2.is_valid(raise_exception=True)
                sr2.save()
                sr3=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['submition_deadline'],"type" :submition_deadline_id,"conference":serializer.data['id']})
                sr3.is_valid(raise_exception=True)
                sr3.save()
                sr4=ConferenceDatesHistorySerializer(data={"date":serializer.validated_data['start_submition_date'],"type" :start_submition_date_id,"conference":serializer.data['id']})
                sr4.is_valid(raise_exception=True)
                sr4.save()
                sr5=ConferenceStatusHistorySerializer(data={"type" :pending_id,"conference":serializer.data['id']})
                sr5.is_valid(raise_exception=True)
                sr5.save()
                for reviewer in serializer.validated_data['reviewers']:
                    nt=notification.objects.create(subject='you are invited to review in conference',type='invitation',invitation_status='pending',conference_id=serializer.data['id'])
                    nt.users_list(reviewer)
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # save the creator in db
            
            

