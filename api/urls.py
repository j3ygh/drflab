from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet
from .views import DeviceViewSet


# Routers provide an easy way of automatically determining the URL conf.
router_crm = routers.DefaultRouter()
router_crm.register('person', PersonViewSet)
router_crm.register('device', DeviceViewSet)

urlpatterns = [
    path('', include((router_crm.urls, 'crm'))),
]