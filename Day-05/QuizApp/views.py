from django.shortcuts import render,redirect
from QuizApp.forms import Usreg,Reg
from QuizApp.models import Stdt
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
	y = Stdt.objects.all()
	if request.method == "POST":
		p = Usreg(request.POST)
		if p.is_valid():
			p.save()
	p = Usreg()
	return render(request,'html/std.html',{'n':p,'h':y})

def userup(request,h):
	k = Stdt.objects.get(id=h)
	if request.method == "POST":
		b = Usreg(request.POST,instance=k)
		if b.is_valid():
			b.save()
		return redirect('/dl')	
	b = Usreg(instance=k)
	return render(request,'html/usptd.html',{'n':b})

def usdl(request,b):
	y = Stdt.objects.get(id=b)
	if request.method == "POST":
		y.delete()
		return redirect('/dl')
	return render(request,'html/usdel.html',{'j':y})

def usrg(request):
	if request.method == "POST":
		u = Reg(request.POST)
		if u.is_valid():
			u.save()	
	u = Reg()
	return render(request,'html/usrt.html',{'b':u})


