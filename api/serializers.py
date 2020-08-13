from rest_framework import serializers
from crm.models import Person
from crm.models import Device


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            # 'url',
            'id',
            'uuid',
            'name',
            'phone_number',
            'remark',
        )
        extra_kwargs = {
            'url': {'view_name': 'api:crm:person-detail'}
        }


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            # 'url',
            'id',
            'uuid',
            'name',
            'os',
            'cpu',
            'ram',
            'remark',
            'customer',
        )
        extra_kwargs = {
            'url': {'view_name': 'api:crm:device-detail'}
        }
