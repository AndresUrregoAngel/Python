#from django.shortcuts import render
from django.contrib.auth import login , authenticate
from local_sites.forms import SingUpForm
from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required 

# Create your views here.
'''
@login_required
def home(request):
	return render (request, 'home.html') 
'''	
@login_required
def home(request):
	if request.user.groups.filter(name="Student").exists():
		return render (request, 'homeStudent.html') 
	else:
		return render (request, 'homeTeacher.html') 
		
		

def singup(request):
	if request.method == 'POST':
		form = SingUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.birth_date = form.cleaned_data.get('birth_date')
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.grade = form.cleaned_data.get('grade')
			group = form.cleaned_data.get('group')
			user.save()
			# group 1 Student - group 2 Teacher
			if (group.lower() == 'student'):
				user.groups.add(1)
			else:
				user.groups.add(2)
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username , password=raw_password)
			login(request,user)
			return redirect('home')
			
	else:
		form = SingUpForm()
	
	return render (request,'singup.html',{'form':form})
	

