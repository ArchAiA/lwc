from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join



def home(request):

	"""USING REGULAR FORMS"""
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created=Join.objects.get_or_create(email=email)
	"""USING REGULAR FORMS"""

	
	"""USING MODEL FORMS"""
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False) #The commit statement allows us to modify before saving data
		#We might do something here
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		#new_join.save()		
	"""USING MODEL FORMS"""


	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

