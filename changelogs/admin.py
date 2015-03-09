from django.contrib import admin
from changelogs.models import Project, Changelog

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ChangelogAdmin(admin.ModelAdmin):
    list_display = ['date','project']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Changelog, ChangelogAdmin)
