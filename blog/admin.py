from django.contrib import admin
from blog.models import Bug,Project,BugModel

# Register your models here.

admin.site.register(Bug)
admin.site.register(Project)
admin.site.register(BugModel)