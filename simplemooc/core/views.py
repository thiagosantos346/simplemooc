from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ContactCourse
# Create your views here.

def home(request):
	return render(request, 'home.html', {'usuario': 'thiago'})

def contato(request):
	if request.method == 'POST':
			form = ContactCourse(request.POST)
			if form.is_valid() :
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				message = form.cleaned_data['message']
				form = ContactCourse()
				return HttpResponseRedirect('/contato/')

	else:
		form = ContactCourse()

	context = {
		'form':ContactCourse()
	}

	return render(request, 'contato.html', {'form':form} )
