from django.urls import path
from QuizApp import views
from django.contrib.auth import views as av

urlpatterns = [
	path('',views.home,name="hm"),
	path('dt/',views.about,name="ab"),
	path('rg/',views.register,name="rgt"),
	path('dl/',views.stdetails,name="v"),
	path('usup/<int:h>/',views.userup,name="up"),
	path('usd/<int:b>/',views.usdl,name="ud"),
	path('thy/',views.usrg,name="us"),
	path('lgo/',av.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgt/',av.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]