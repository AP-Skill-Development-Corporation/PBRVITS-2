from django.urls import path
from QuizApp import views

urlpatterns = [
	path('',views.home),
]