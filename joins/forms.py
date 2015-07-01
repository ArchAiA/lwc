from django import forms

from .models import Join


class EmailForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()

#All this form does is take the form fields from an associated model (imported at top)	
class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email"]