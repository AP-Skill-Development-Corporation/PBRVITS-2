from django.shortcuts import render
from QuizApp.forms import Usreg
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		u = request.POST['usn']
		p = request.POST['pwd']
		ro = request.POST['rn']
		return render(request,'html/details.html',{'us':u,'rl':ro})
	return render(request,'html/register.html')

def stdetails(request):
	p = Usreg()
	return render(request,'html/std.html',{'n':p})


