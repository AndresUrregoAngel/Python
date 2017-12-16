#from django.shortcuts import render
from django.contrib.auth import login , authenticate
from django.shortcuts import render , redirect 

# Create your views here.
'''
def singup(request):
	if request.method == 'POST':
		form = SingUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_form.save()
			user.profile.birth_date = form.cleaned_date.get('birth_date')
			user.save()			
			raw_password = form.cleaned_date.get('password1')
			user = authenticate(username=user.username , password=raw_password1)
			login(request,user)
			return redirect('home')
			
	else:
		form = SingUpForm()
	
	return render (request,'singup.html',{'form':form})

'''

def exercises(request):
	return render (request,'exercises.html')