from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join


"""L24: GET IP"""
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip
"""L24: GET IP"""




def home(request):

	# """L24 WAYS TO GET DATA IN THE REQUEST"""
	# print request.META.get('HTTP_CONNECTION')
	# print request.META.get("HTTP_X_FORWARDED_FOR")
	# """L24 WAYS TO GET DATA IN THE REQUEST"""


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
		# #We might do something here
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if create:
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		#redirect here

		# new_join.ip_address=get_ip(request)
		# new_join.save()		
	"""USING MODEL FORMS"""


	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

