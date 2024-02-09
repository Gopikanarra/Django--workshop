from django.shortcuts import render,redirect
from .models import Student,Employee
from .forms import EmForm
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'index1.html')

def about(request):
	return render(request,'demo.html')

def student(request):
	data = Student.objects.all()
	if request.method=="POST":
		n=request.POST['name']
		r=request.POST['roll']
		t=request.POST['numm']
		r=Student(rn=r,sn=n,sy=t)
		r.save()
		return redirect('/st/') 
	return render(request,'student.html',{'d':data})
def stdup(req,k):
	c=Student.objects.get(id=k)
	if req.method=="POST":
		c.rn=req.POST['roll']
		c.sn=req.POST['name']
		c.sy=req.POST['numm']
		c.save()
		return redirect('/st')
	return render(req,'stdup.html',{'v':c})
def sdele(request,m):
	h=Student.objects.get(id=m)
	if request.method=="POST":
		h.delete()
		return redirect('/st')
	return render(request,'delete.html',{'y':h})

def employee(request):
	u=Employee.objects.all()
	if request.method=="POST":
		q=EmForm(request.POST)
		if q.is_valid():
			q.save()
			messages.success(request,"employee Created Successfully!!")
			return redirect('/em')
	q=EmForm()
	return render(request,'empy.html',{'d':q,'r':u})

def empup(req,d):
	a=Employee.objects.get(id=d)
	if req.method=="POST":
		n=EmForm(req.POST,instance=a)
		if n.is_valid():
			a.save()
			messages.info(req,"employee updated Successfully!!")
			return redirect('/em')
	n=EmForm(instance=a)
	return render(req,'emupdate.html',{'k':n})


def dels(req,j):
	j=Employee.objects.get(id=j)
	if req.method=="POST":
		j.delete()
		messages.warning(req,"employee Deleted Successfully!!")
		return redirect('/em')
	return render(req,'dell.html',{'b':j})

