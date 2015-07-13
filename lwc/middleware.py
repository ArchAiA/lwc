"""L27: Using Custom Middleware"""
from joins.models import Join


class ReferMiddleware():
	def process_request(self, request):
		#print request
		# try:
		# 	ref_id = request.GET.get("ref", "")
		# except:
		# 	ref_id = False
		ref_id = request.GET.get("ref", "")
		# print ref_id
		try:
			obj = Join.objects.get(ref_id=ref_id) #We are getting the Join object where the ref_id is equal to the ref_id beign passed in the url
		except:
			obj = None
		
		if obj:
			request.session['join_id_ref'] = obj.id #This is setting a session variable called 'ref' equal to obj, which is the ref_id passed in the url



"""L27: Using Custom Middleware"""
