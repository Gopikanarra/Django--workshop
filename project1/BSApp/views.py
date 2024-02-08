from django.shortcuts import render,redirect
from .models import Student
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