from django.contrib import admin
from .models import Person
from .models import Device


admin.site.register(Person)
admin.site.register(Device)