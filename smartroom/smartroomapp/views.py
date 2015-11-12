from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .forms import ProjectForm
from .models import ProjectModel
from .serializers import ProjectSerializer


# Create your views here.

class ProjectView(View):

	def get(self, request, *args, **kwargs):
		pass

	def post(self, request, *args, **kwargs):
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			# new_project = ProjectModel(title=request.POST['title'], description=request.POST['description'], project_file=request.FILES['project_file'])
			# new_project.save()
			form.save()
			return HttpResponse("Successful", status=200)

		return HttpResponse("Error", status=400)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(ProjectView, self).dispatch(*args, **kwargs)


class ProjectAPIView(generics.ListAPIView):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer
