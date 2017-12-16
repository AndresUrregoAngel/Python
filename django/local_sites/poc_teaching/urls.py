from django.conf.urls import url
#from . import views
from poc_teaching import views as poc_views


urlpatterns = [
	
	url('exercises/$',poc_views.exercises,name ='exercises'),
	

]