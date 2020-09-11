from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet
from .views import DeviceViewSet
from .views import CallLogViewSet
from .views import UserProfileViewSet
from .views import hello_world


# Routers provide an easy way of automatically determining the URL conf.
router_crm = routers.DefaultRouter()
# router_crm.register('person', PersonViewSet)
# router_crm.register('device', DeviceViewSet)
router_crm.register('calllog', CallLogViewSet)
router_crm.register('userprofile', UserProfileViewSet)

urlpatterns = [
    path('', include((router_crm.urls, 'crm'))),
    path('hello-world/', hello_world, name='hello_world'),
]
