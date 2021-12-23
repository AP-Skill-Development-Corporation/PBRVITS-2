from django.urls import path
from QuizApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('dt/',views.about,name="ab"),
	path('rg/',views.register,name="rgt"),
	path('dl/',views.stdetails,name="v"),
]