from django.forms import ModelForm
from QuizApp.models import Stdt,User
from django import forms
from django.contrib.auth.forms import UserCreationForm

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

class Reg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username"
			}),
		}







