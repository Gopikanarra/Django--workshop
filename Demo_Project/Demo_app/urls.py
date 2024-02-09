from django.urls import path
from Demo_app import views
urlpatterns = [
    path('',views.home,name="hm"),
    path('reg/',views.usreg,name="ug"),
]