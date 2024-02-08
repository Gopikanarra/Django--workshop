from django.urls import path;
from BSApp import views
urlpatterns=[
	path('',views.home,name="home"),
	path('ab/',views.about,name="abt"),
	path('st/',views.student,name="std"),
	path('ups/<int:k>/',views.stdup,name="stpd"),
	path('sdel/<int:m>/',views.sdele,name="sdele"),
]