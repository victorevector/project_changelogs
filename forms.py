from django import forms
from django.forms import ModelForm, Textarea
from changelogs.models import Project, Changelog
from django.contrib.auth.models import User

class ChangelogForm(forms.ModelForm):
    class Meta:
        model = Changelog
        fields = ('project','date','log')

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'slug']
class UserForm(forms.ModelForm):
    #hides the password input when user types it in:
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
