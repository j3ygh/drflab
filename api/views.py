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

    def record_call_log(self, request):
        CallLog.objects.create(
            path=request.path,
            method=request.method,
            params=str(dict(request.GET)),
            data=str(dict(request.POST)),
            meta=str(request.META),
            called_by=request.user,
        )

    def create(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.record_call_log(request)
        return super().list(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
