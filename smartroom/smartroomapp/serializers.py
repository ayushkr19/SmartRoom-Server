from rest_framework import serializers
from .models import ProjectModel

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectModel
		fields = ('author', 'title', 'description', 'project_file')