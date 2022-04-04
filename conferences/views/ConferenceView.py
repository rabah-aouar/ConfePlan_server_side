
from rest_framework import status
from conferences.models import Conference
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from conferences.serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

class ConferenceView(GenericAPIView):
    serializer_class=ConferenceDetailSerializer
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
            serializer= ConferenceDetailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.errors
            # save the creator in db
            serializer.validated_data['creator']=request.user
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            


