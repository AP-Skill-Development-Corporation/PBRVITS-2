from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	t = {
		(1,'Student'),
		(2,'Teacher'),
		(3,'Guest')
	}
	age = models.IntegerField(default=18)
	usrole = models.IntegerField(choices=t,default=3)

class Stdt(models.Model):
	username = models.CharField(max_length=50)
	rollnumber = models.CharField(max_length=20)
	year = models.IntegerField(default=1)
	