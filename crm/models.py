from django.db import models
import uuid


def get_default_uuid():
    return uuid.uuid4().hex[:8]


class Person(models.Model):

    id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    uuid = models.CharField(
        verbose_name='UUID',
        max_length=63,
        default=get_default_uuid,
        editable=False,
    )
    name = models.CharField(
        verbose_name='Name',
        blank=True,
        max_length=63,
    )
    phone_number = models.CharField(
        verbose_name='Phone Number',
        blank=True,
        max_length=63,
    )
    remark = models.CharField(
        verbose_name='Remark',
        blank=True,
        max_length=255,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.uuid if self.name == '' else f'{self.name} ({self.uuid})'


class Device(models.Model):

    id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    uuid = models.CharField(
        verbose_name='UUID',
        max_length=63,
        default=get_default_uuid,
        editable=False,
    )
    name = models.CharField(
        verbose_name='Name',
        blank=True,
        max_length=63,
    )
    os = models.CharField(
        verbose_name='OS',
        blank=True,
        max_length=50,
    )
    cpu = models.IntegerField(
        verbose_name='CPU',
        blank=True,
        null=True,
    )
    ram = models.IntegerField(
        verbose_name='RAM (GB)',
        blank=True,
        null=True,
    )
    remark = models.CharField(
        verbose_name='Remark',
        blank=True,
        max_length=400,
    )
    customer = models.ForeignKey(
        verbose_name='Customer',
        blank=True,
        null=True,
        to='Person',
        on_delete=models.CASCADE,
        related_name='whose_%(model_name)s_customer',
    )

    class Meta():
        ordering = ['id']
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.uuid if self.name == '' else f'{self.name} ({self.uuid})'


class CallLog(models.Model):

    id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    uuid = models.CharField(
        verbose_name='UUID',
        max_length=63,
        default=get_default_uuid,
        editable=False,
    )
    url = models.CharField(
        verbose_name='Request URL',
        max_length=511,
    )
    data = models.CharField(
        verbose_name='Request data',
        max_length=511,
    )
    called_by = models.ForeignKey(
        verbose_name='Called by',
        blank=True,
        null=True,
        to='Person',
        on_delete=models.CASCADE,
        related_name='whose_%(model_name)s_customer',
    )

    class Meta():
        ordering = ['id']
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.uuid if self.name == '' else f'{self.name} ({self.uuid})'
