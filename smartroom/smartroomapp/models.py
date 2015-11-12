from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join("projects", "%s" % instance.author, filename)

# Create your models here.
class ProjectModel(models.Model):
	author = models.CharField(max_length=30)
	title = models.CharField(max_length=50, unique=True)
	description = models.CharField(max_length=200)
	project_file = models.FileField(upload_to=get_upload_path)


