1. pip install virtualenv
2. pip install virtualenvwrapper-win
3. mkvirtualenv --python=C:\Users\a_urrego\AppData\Local\Programs\Python\Python36-32\python.exe djangopoc
4. workon djangopoc
5. pip install django
6. django-admin  --version

------------creating a project

1. create a site: django-admin startproject mysite
2. go into the project repository (CD mysite)
3. python manage.py runserver
4. create your app python manage.py startapp polls
5. Edit the views.py file with:
	from django.http import HttpResponse


	def index(request):
	    return HttpResponse("Hello, world. You're at the polls index.")

6. create manually the file urls.py in your polls application
	create this content in the file:
	
	from django.urls import path

	from . import views

	urlpatterns = [
		    path('', views.index, name='index'),
			]

7. Edit mysite/urls.py and whithin the method urlpatterns includes a path for pools app
	from django.contrib import admin
	from django.urls import include,path

	urlpatterns = [
		path('polls/', include('polls.urls')),
		path('admin/', admin.site.urls), ]


8. run the server again  python manage.py runserver


documentation:
https://docs.djangoproject.com/en/2.0/

-------------------- Beanstalk
documentation: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-init.html


1. pip install awsebcli / eb --version
2. pip freeze >requirements.txt
3. eb init
4. mkdir .ebextensions
5. touch django.config
	5.1 vim django.config
	option_settings:
		  aws:elasticbeanstalk:container:python:
		  WSGIPath: mysite/wsgi.py

6. go to the file settings.py and ALLOWED_HOSTS = ['mysitepoc.us-west-2.elasticbeanstalk.com']

-------------- configuring eb cli
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-getting-started.html







