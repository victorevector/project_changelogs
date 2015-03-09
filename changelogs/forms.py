from django import forms
from changelogs.models import Project, Changelog

class ChangelogForm(forms.ModelForm):
    class Meta:
        model = Changelog
        fields = ['project', 'date', 'log']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'slug']
