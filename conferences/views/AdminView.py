from ast import Delete
from rest_framework.views import APIView
from rest_framework.response import Response
from conferences.models import Conference, ConferenceStatus
from conferences.serializers.ConferenceStatusHistorySerializer import ConferenceStatusHistorySerializer
from notifications.models import notification
from users.models import User
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView
from conferences.serializers.AccepteConferenceSerializer import AccepteConferenceSerializer

class AdminView(GenericAPIView):
    permission_classes=[IsAdminUser] #only admins can use this view(end point)
    serializer_class=AccepteConferenceSerializer
    
    #accpte conference status='accepted'
    #refuse conference status='refused'
    #by default pending
    def put(self, request ,id):
        serializer=AccepteConferenceSerializer(data=request.data)
        accepted=ConferenceStatus.objects.get_or_create(status='accepted')
        accepted_id=accepted[0].id
        refused=ConferenceStatus.objects.get_or_create(status='refused')
        refused_id=refused[0].id
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        try:
            conference=Conference.objects.get(id=id)
            conference.status=serializer.data['status']
            conference.save()
            nt=notification.objects.create(subject='your request of conference '+conference.title+' is '+conference.status ,type='normal',conference_id=conference.id)
            nt.users_list.add(conference.creator)
            if serializer.data.get('status')=="accepted":
                sr5=ConferenceStatusHistorySerializer(data={"type" :accepted_id,"conference":id})
            else:
                sr5=ConferenceStatusHistorySerializer(data={"type" :refused_id,"conference":id})
            sr5.is_valid(raise_exception=True)
            sr5.save()
            return Response(status=status.HTTP_200_OK)
        except:
            #conference doesn't exist(wrong id)
            return Response(status=status.HTTP_404_NOT_FOUND)

    #delete conference by admin 
    def delete(self,request,id):
        try:
            conference=Conference.objects.get(id=id)
            conference.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            #conference doesn't exist(wrong id)
            return Response(status=status.HTTP_404_NOT_FOUND)
