from django import forms
from .models import Vote

class voteForm(forms.ModelForm):
	class Meta:
		model = Vote
		fields = ['candidate',]
	def __init__(self,candidates, *args, **kwargs):
		super(voteForm,self).__init__(*args, **kwargs)
		self.fields['candidate'] = forms.ChoiceField(choices=candidates, widget=forms.RadioSelect)