# from reports.models.Report import *
from reports.serializers.reportSerializers import *
from rest_framework import generics


class ReportView(generics.CreateAPIView):
    serializer_class = ReportSerializer
