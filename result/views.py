from django.shortcuts import render,redirect
import sys
sys.path.insert(1,'/usr/share/doc/python3-fingerprint/examples')
import example_search
from register.models import Candidate, Voter
# from result.models import Vote
from register.forms import candidateForm, voterForm

# Create your views here.
def index(request):
	context={}
	candidates=Candidate.objects.all().order_by('region')
	prev=0
	context['regions']=[]
	temp=[]
	for cand in candidates:
		if(prev==cand.region):
			temp.append(cand)
		else:
			if(prev!=0):
				context['regions'].append(temp)
			prev=cand.region
			temp=[]
			temp.append(cand)
	context['regions'].append(temp)
	print(context)
	print("$$$$$$$$$$$$$$$")
	return render(request,'result/index.html',context)
