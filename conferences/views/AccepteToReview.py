
from rest_framework import status
from conferences.models import Conference
from ..serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from ..serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from ..serializers.ConferenceModificationSerializer import ConferenceModificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from notifications.models import notification

class AccepteToReview(GenericAPIView):
    serializer_class=()
    parser_classes = (FormParser, MultiPartParser)
    def post(self,request,id):
        try:
            notification1=notification.objects.get(id=id)
            notification1.invitation_status="accepted"
            notification1.save()
            conference=Conference.objects.get(id=notification1.conference_id)
            user=notification1.users_list.all().first()
            conference.reviewers.add(user)
            return Response(status=status.HTTP_200_OK)
        except:
            ##conference doesn't exist(wrong id)
            return Response(status=status.HTTP_404_NOT_FOUND)