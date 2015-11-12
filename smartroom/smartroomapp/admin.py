from django.contrib import admin
from .models import ProjectModel

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')


admin.site.register(ProjectModel, ProjectAdmin)
