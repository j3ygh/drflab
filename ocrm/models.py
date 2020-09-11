from django.db import models


class UserProfile(models.Model):

    chief_id = models.CharField(
        max_length=20,
        primary_key=True,
    )
    nick_name = models.CharField(
        max_length=100
    )
    gender = models.IntegerField(null=True)
    birthday = models.DateField()
    group_id = models.IntegerField(null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    blood_type = models.CharField(
        max_length=5
    )
    member_level = models.CharField(
        max_length=5
    )
    disabled = models.CharField(
        max_length=5
    )
    ext_date_time = models.DateField(null=True)
    abdominal_circumference = models.IntegerField(null=True)
    marriage = models.IntegerField(null=True)
    user_seq = models.IntegerField(null=True)

    class Meta():
        db_table = 'USER_PROFILE'
        managed = False
