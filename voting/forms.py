from django import forms
from .models import Vote

class voteForm(forms.Form):
	candidate=forms.IntegerField()
	