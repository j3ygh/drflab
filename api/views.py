from rest_framework import viewsets
from crm.models import Person
from .serializers import PersonSerializer
from crm.models import Device
from .serializers import DeviceSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
