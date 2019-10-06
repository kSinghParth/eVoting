from django.shortcuts import render,redirect

from register.models import Candidate, Voter
from register.forms import candidateForm, voterForm

# Create your views here.
def voter(request):
	context={}
	if request.method=='POST':
		form = voterForm(request.POST)
		if form.is_valid():
		    form.save(commit=True)
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