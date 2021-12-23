from django.db import models

# Create your models here.

class Stdt(models.Model):
	username = models.CharField(max_length=50)
	rollnumber = models.CharField(max_length=20)
	year = models.IntegerField(default=1)
	