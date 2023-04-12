from django.db import models

# Create your models here.

class tUser(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    age = models.IntegerField()
    tell = models.IntegerField(null=True)
    active = models.BooleanField(null=True)
    description = models.TextField(null=True)
    # t = models.OneToOneField('app_2.tPosition', on_delete=models.SET_NULL, null=True)
    # t = models.ForeignKey('app_2.tPosition', on_delete=models.SET_NULL, null=True)
    # t = models.ManyToManyField('app_2.tPosition')