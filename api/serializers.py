from rest_framework import serializers
from crm.models import Person
from crm.models import Device
from crm.models import CallLog
from ocrm.models import UserProfile


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'url',
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
            'url',
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


class CallLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = (
            'id',
            'uuid',
            'path',
            'method',
            'params',
            'data',
            'meta',
            'called_by',
        )
        extra_kwargs = {
            'url': {'view_name': 'api:crm:calllog-detail'}
        }


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'chief_id',
            'nick_name',
            'gender',
            'birthday',
            'group_id',
            'height',
            'weight',
            'blood_type',
            'member_level',
            'disabled',
            'ext_date_time',
            'abdominal_circumference',
            'marriage',
            'user_seq',
        )
        extra_kwargs = {
            'url': {'view_name': 'api:crm:userprofile-detail'}
        }
