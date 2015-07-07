from django.shortcuts import render, HttpResponseRedirect

from .forms import EmailForm, JoinForm
from .models import Join

import uuid

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


def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id




def share(request, ref_id):
	print ref_id
	context = {"ref_id":ref_id}
	template = "share.html"
	return render(request, template, context)





def home(request):

	"""USING MODEL FORMS"""
	form = JoinForm(request.POST or None) #this creates an instance of JoinForm called form
	if form.is_valid():
		new_join = form.save(commit=False) #The commit statement allows us to modify before saving data
		email = form.cleaned_data['email'] #this takes the email from the form for the creation of new_join_old in the next line
		new_join_old, created = Join.objects.get_or_create(email=email) #This creates an instance of Join and uses the email field from the form
		if created: #if the email already exists, the attributes of the new instance of Join are set below
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request) #get ip address
			new_join_old.save()
		return HttpResponseRedirect("/%s" % (new_join_old.ref_id))
		
	"""USING MODEL FORMS"""


	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

