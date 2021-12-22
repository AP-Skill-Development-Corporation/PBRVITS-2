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











