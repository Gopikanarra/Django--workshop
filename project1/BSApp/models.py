from django.db import models
# Create your models here.
class Student(models.Model):
	rn=models.CharField(max_length=12)
	sn=models.CharField(max_length=150)
	sy=models.IntegerField(default=18)	

class Employee(models.Model):
	desig=[
			('0','--select Designation--'),
			('1','Intern'),
			('2','Assistant Professor'),
			('3','Professor'),
			('4','Trainee'),
			('5','Manager'),
	]
	eid=models.CharField(max_length=20)
	ename=models.CharField(max_length=120)
	edept=models.CharField(max_length=50)
	edesig=models.CharField(choices=desig,default='0',max_length=5)

	def __str__(self):
		return self.ename