from django.contrib import admin

# Register your models here.
from .models import Join 
# from .models import JoinFriends

class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'friend', 'timestamp', 'updated']
	class Meta:
		model = Join



admin.site.register(Join, JoinAdmin)
# admin.site.register(JoinFriends)