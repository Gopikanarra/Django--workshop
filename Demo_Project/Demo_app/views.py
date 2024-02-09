from django.shortcuts import render
from .forms import UsRegForm
# Create your views here.
def home(req):
	return render(req,'html/home.html')

def usreg(req):
	t=UsRegForm()
	return render(req,'html/register.html',{'p':t})