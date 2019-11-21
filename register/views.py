from django.shortcuts import render,redirect
import datetime
from django.utils import timezone
from register.models import Candidate, Voter
from register.forms import candidateForm, voterForm
import sys
sys.path.insert(1,'/usr/share/doc/python3-fingerprint/examples')
import example_enroll

# Create your views here.
def voter(request):
	context={}
	if request.method=='POST':
		form = voterForm(request.POST)
		if form.is_valid():
                    fingerP=example_enroll.pro()
                    print("################")
                    print(fingerP)
                    print((datetime.datetime.now(timezone.utc)-form.cleaned_data['dob']).total_seconds())
                    voter=form.save(commit=False)
                    voter.finger=fingerP
                    if(fingerP>0):
                        voter.save()
		return redirect('/register')
	else:
		form = voterForm()
	context['form']=form
	return render(request,'register/voter.html',context)
        
def candidate(request):
	context={}
	if request.method=='POST':
		form = candidateForm(request.POST)
		if form.is_valid():
		    can=form.save(commit=False)
		    can.votes=0
		    can.save()
		return redirect('/register/candidate')
	else:
		form = candidateForm()
	context['form']=form
	return render(request,'register/candidate.html',context)