# from django.contrib.auth import validators
from django.core import validators
from django.db import models


class Create(models.Model):
    choice = [('male', 'MALE'), ('female', 'FEMALE')]
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile_no = models.CharField(max_length=20, validators=[validators.RegexValidator('[7-9]{1}+[0-9]{9}')])
    gender = models.CharField(max_length=10, choices=choice)

