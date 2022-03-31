
from rest_framework import status
from conferences.models import Conference
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from conferences.serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ConferenceView(GenericAPIView):
    serializer_class=ConferenceDetailSerializer
    def get(self,request):
        try:
            conferences=Conference.objects.all()
        except:
            return Response({},status=status.HTTP_404_NOT_FOUND)
        if not conferences is None:
            return Response(data=ConferenceDetailSerializer(conferences,many=True).data,status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_200_OK)

    def post(self, request):
            serializer= ConferenceDetailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.errors
            # save the creator in db
            serializer.validated_data['creator']=request.user
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            


