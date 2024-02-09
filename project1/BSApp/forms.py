from .models import Employee
from django import forms

class EmForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=["ename","eid","edept","edesig"]
		widgets={
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee ID",
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Name",
			}),
		"edept":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Deptartment",
			}),
		"edesig":forms.Select(attrs={
			"class":"form-control my-2",
			})
		}
