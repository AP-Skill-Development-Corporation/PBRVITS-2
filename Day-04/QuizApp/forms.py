from django.forms import ModelForm
from QuizApp.models import Stdt
from django import forms

class Usreg(ModelForm):
	class Meta:
		model = Stdt
		fields = ["username","rollnumber","year"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username"
			}),
		"rollnumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter RollNumber"
			}),
		"year":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Year"
			}),
		}