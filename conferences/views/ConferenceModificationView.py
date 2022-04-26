
from rest_framework import status
from conferences.models import Conference
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
            if conference.creator==request.user:
                serializer = ConferenceModificationSerializer(conference, data=request.data)
                if serializer.is_valid():
                    serializer.save()
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