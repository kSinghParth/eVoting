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
	voterid=1
	context['voter']=Voter.objects.get(id=voterid)
	request.session['id']=voterid
	candidates=Candidate.objects.filter(region=context['voter'].region).values_list('id','name')
	context['candidates']=candidates
	form = voteForm()
	context['form']=form
	return render(request,'voting/index.html',context)
