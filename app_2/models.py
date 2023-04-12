from django.db import models

# Create your models here.

class tPosition(models.Model):
    STATUS = [
        ('boss', 'BOSS'),
        ('std', 'Student')
	]

    position = models.CharField(max_length=60)
    status = models.CharField(max_length=60, choices=STATUS, default='std')