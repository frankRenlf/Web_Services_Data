from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    gender_choices = (
        (0, "female"),
        (1, "male"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField()
    # delete relevant user
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    # remove depart_id
    depart = models.ForeignKey(to="Department", to_fields="id", null=True, blank=True, on_delete=models.SET_NULL)
