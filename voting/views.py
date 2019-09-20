from django.shortcuts import render,redirect
from register.models import Candidate, Voter
from voting.models import Vote
from voting.forms import voteForm
from django.http import HttpResponse

def index(request):
	context={}
	if request.method=='POST':
		form = voteForm(request.POST)
		if form.is_valid():
			# do something with data
			return HttpResponse('Success')
	voterid=1
	context['voter']=Voter.objects.get(id=voterid)
	request.session['id']=voterid
	candidates=Candidate.objects.filter(region=context['voter'].region).values_list('id','name')
	form = voteForm(candidates)
	context['form']=form
	return render(request,'voting/index.html',context)
