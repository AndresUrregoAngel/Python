from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=True)
	last_name = forms.CharField(max_length=30,required=True)
	grade = forms.CharField(max_length=30,required=False , help_text='Current school grade - just students')
	group = forms.CharField(max_length=30,required=True , help_text='Please type teacher or student according to your profile')
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	
	
	class Meta:
		model = User
		fields = ('username','first_name','last_name','grade','group','birth_date','password1','password2',)