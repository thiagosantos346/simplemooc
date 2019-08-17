from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from  .models import  Course
from  .forms  import ContactCourse

# Create your views here.

def index(request):
	courses = Course.objects.all()
	tamplate_name = 'cursos/index.html'
	context = {
		'courses':courses
	}
	return render(request, tamplate_name, context)


def details(request, atalho):
	course  = get_object_or_404(Course, slug=atalho)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form = ContactCourse()
	else:
		form = ContactCourse()

	context['form'] = form
	context['Course'] = Course
	tamplate_name = 'cursos/details.html'

	return render(request, tamplate_name, context)
