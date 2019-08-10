from django.db import models
import datetime

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=500, null=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state = models.ForeignKey('State', null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=datetime.date.today)
    groups = models.ManyToManyField('Group')

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
