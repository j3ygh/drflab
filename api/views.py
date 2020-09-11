from rest_framework import viewsets
from crm.models import Person
from .serializers import PersonSerializer
from crm.models import Device
from .serializers import DeviceSerializer
from crm.models import CallLog
from .serializers import CallLogSerializer
from ocrm.models import UserProfile
from .serializers import UserProfileSerializer
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


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        CallLog.objects.create(
            path=request.path,
            params=str(dict(request.GET)),
            data=str(dict(request.POST)),
            called_by=request.user,
        )
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        CallLog.objects.create(
            path=request.path,
            params=str(dict(request.GET)),
            data=str(dict(request.POST)),
            called_by=request.user,
        )
        return super().create(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
