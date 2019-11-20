from django import forms
from .models import Candidate, Voter
from django.forms import ModelForm

class candidateForm(ModelForm):
    class Meta:
        model = Candidate 
        fields = ('name', 'region',)


class voterForm(ModelForm):
    class Meta:
        model = Voter 
        fields = ('name', 'region','dob','address','father_name')
        widgets = {'dob': forms.DateInput(attrs={'class':'datepicker'}),}
