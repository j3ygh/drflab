from rest_framework import viewsets
from crm.models import Person
from .serializers import PersonSerializer
from crm.models import Device
from .serializers import DeviceSerializer
from crm.models import CallLog
from .serializers import CallLogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CallLogViewSet(viewsets.ModelViewSet):
    queryset = CallLog.objects.all()
    serializer_class = CallLogSerializer


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
