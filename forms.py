from django import forms
from .models import List

#Creates the class ListForm wich takes instanitaties that class Meta
#The Meta class sets the var model = List with the fields "item, and completed"
class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields= {"item", "completed"}
