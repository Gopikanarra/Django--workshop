from django.shortcuts import render
from django.http import HttpResponse

#views.py contains the logic for handling requests, and urls.py maps URLs to specific views in your Django project.
# Together, they define how your web application responds to different URLs.

# Create your views here.

def greet(sd,n):
	return HttpResponse(f"Hi Welcome {n}")


def stdnt(request,a,b,c="VVIT"):
	return HttpResponse(f"College Name:{c}<br/>Student Name:{a}<br>Student Age:{b}")

def ky(s):
	return HttpResponse("<h3>Welcome User</h3>")

def my(sd,n):
	return HttpResponse(f"<h1>hi<span style='color:red'>{n}</span></h1>")

def emp(t,es,en):
		return HttpResponse("<style>#w{color:lightpink}</style><h2>welcome<span style='color:red'> employee "+en+"</span></h2><h3>salary:<span id='w'>"+str(es)+"</span></h3>")

def home(req,a,b):
	return HttpResponse("<html><body><hidden><h3 id='h'>Hello i am <span style='color:red'>"+ a +"</span> i am good at <span style='color:blue'> "+ b +"</span></h3></hidden></body><script>alert(document.getElementById('h').innerText);</script></html>")

def tables(r,name,roll,branch,year):
	return HttpResponse(f"<html><body><table border='1'><tr><td>Name</td><td>{name}</td></tr><tr><td>roll number </td><td>{roll}</td></tr><tr><td>branch</td><td>{branch}</td></tr><tr><td>year</td><td>{year}</td></tr></table></body></html>")

# def func(req,name,role):
# 	return render(req,'index.html',{'n':name,'r':role})

def employee(request,name,salary,company,designation):
	return render(request,'emp.html',{'na':name,'sa':salary,'com':company,'des':designation})


# def home(req, a, b):
#     return HttpResponse("<html><body><h3 id='h'>Hello i am <span style='color:red'>" + a + "</span> i am good at <span style='color:blue'> " + b + "</span></h3><script>alert(document.getElementById('h').innerText);</script></body></html>")

# def home(req, a, b):
#     return HttpResponse("<script>alert(document.getElementById('h').innerText);</script><body><h3 id='h'>Hello i am <span style='color:red'>" + a + "</span> i am good at <span style='color:blue'> " + b + "</span></h3></body>")


# 07-02-2024

def forms(request):
	if request.method=="POST":
		name=request.POST['name']
		roll=request.POST['roll']
		acc=request.POST['acc']
		br=request.POST['br']
		print(name)
		print(roll)
		print(acc)
		print(request.POST['br'])
		return render(request,'stdata.html',{'n':name,'r':roll,'a':acc,'b':br})


	return render(request,'stdform.html')
