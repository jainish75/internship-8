# forms.py
from django import forms
from .models import *

from .models import appoint_beauty,Appoint
class AppointForm(forms.ModelForm):
	class Meta:
		model = appoint_beauty
		fields = "__all__"

# class ContactForm(forms.ModelForm):
# 	class Meta:
# 		model = Contact
# 		fields = "__all__"


