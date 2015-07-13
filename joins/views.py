from django.conf import settings #for SHARE_URL
from django.shortcuts import render, HttpResponseRedirect, Http404

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
	# print ref_id
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		#ref_url = "http://127.0.0.1:8000/?ref=%s" % (join_obj.ref_id)
		ref_url = settings.SHARE_URL + join_obj.ref_id
		context = {"ref_id":join_obj.ref_id, "count":count, "ref_url":ref_url}
		template = "share.html"
		return render(request, template, context)
	except:
		raise Http404




def home(request):

	"""L27: Using Custom Middleware"""
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print "The object is: %s" % (obj.email)		
	except:
		obj = None
	"""L27: Using Custom Middleware"""


	"""USING MODEL FORMS"""
	form = JoinForm(request.POST or None) #this creates an instance of JoinForm called form
	if form.is_valid():
		new_join = form.save(commit=False) #The commit statement allows us to modify before saving data
		email = form.cleaned_data['email'] #this takes the email from the form for the creation of new_join_old in the next line
		new_join_old, created = Join.objects.get_or_create(email=email) #This creates an instance of Join and uses the email field from the form
		if created: #if the email already exists, the attributes of the new instance of Join are set below
			new_join_old.ref_id = get_ref_id()
			#add our friend who referred uso to our join model or a related model
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request) #get ip address
			new_join_old.save()

		#Print all "friends" that joined as a result of owner email
		# print Join.objects.filter(friend=obj).count()
		# print obj.referral.all()

		return HttpResponseRedirect("/%s" % (new_join_old.ref_id))
		
	"""USING MODEL FORMS"""


	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

