from django.utils import timezone
from datetime import datetime
from django.shortcuts import render,redirect
from register.models import Candidate, Voter
from voting.models import Vote
from voting.forms import voteForm
from django.http import HttpResponse
import sys
sys.path.insert(1,'/usr/share/doc/python3-fingerprint/examples')
import example_search

def index(request):
	context={}
	if request.method=='POST':
		form = voteForm(request.POST)
		if form.is_valid():
			candidates=Candidate.objects.filter(region=Voter.objects.get(id=request.session['id']).region).values_list('id')
			for candidate in candidates:
				if(candidate[0]==form.cleaned_data['candidate']):
					voted=Vote(voter=request.session['id'],candidate=form.cleaned_data['candidate'])
					candidate=Candidate.objects.get(id=form.cleaned_data['candidate'])
					candidate.votes=int(candidate.votes)+1
					candidate.save()
					voted.save()
					return HttpResponse('Success')
			context['error']="Enter valid id"
			return render(request,'voting/index.html',context)
	voterid=example_search.pro()
	context['showform']=1
	if voterid <0:
            voterid=100
            context['showform']=0
	context['voter']=Voter.objects.get(finger=voterid)
	
	print('*************************************')
	if ((datetime.now(timezone.utc)-context['voter'].dob).total_seconds()/(365*86400)<18):
            context['error']="Underage bitch"
            context['showform']=0
	print(context['voter'].finger)
	check=Vote.objects.filter(voter=context['voter'].id)
	print(len(check))
	if(len(check)>0):
           context['error']="Already Voted"
           context['showform']=0
	request.session['id']=context['voter'].id
	candidates=Candidate.objects.filter(region=context['voter'].region).values_list('id','name')
	context['candidates']=candidates
	form = voteForm()
	context['form']=form
	return render(request,'voting/index.html',context)
