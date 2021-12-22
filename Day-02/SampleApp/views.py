from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	return HttpResponse("hi abdul, how r u")

def hello(request):
	return HttpResponse("hello welcome")

def dt(request,r):
	return HttpResponse("Hi User {}".format(r))

def bt(request,j,n):
	return HttpResponse("Hi User: {}<br/>your number is: {}".format(n,j))

def yu(request,m,u,t):
	return HttpResponse("<h4>Entered Name is: <span style='color:green'>{}</span></h4><h5>Entered Year is: <span style='color:blue'>{}</span></h5><h5>Entered Age is: <span style='color:red'>{}</span></h5>".format(m,u,t))

def k(request,p):
	return HttpResponse("<html><head><title>Html Structure</title></head><body><h3>entered Name is: {}</h3></body></html>".format(p))

def htmlmsg(request):
	return render(request,'html/htmlmsg.html')

def gy(request,m):
	return render(request,'html/data.html',{'p':m})

def gu(request,rt,nm):
	ct = {'a':rt,'b':nm}
	return render(request,'html/gt.html',ct)










