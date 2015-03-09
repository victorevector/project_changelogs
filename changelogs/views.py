from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from changelogs.models import Project, Changelog
from changelogs.forms import ChangelogForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    project_list = Project.objects.order_by('name')
    context_dict = {'projects': project_list}
    return render(request, 'changelogs/index.html', context_dict)

def changelog(request, project_name_slug):
    project = Project.objects.get(slug=project_name_slug)
    logs = Changelog.objects.filter(project = project).order_by('-date')
    context_dict = { 'project': project, 'logs': logs,}
    return render(request,'changelogs/changelog.html', context_dict)

@login_required
def addlog(request, project_name_slug):
    try:
        project = Project.objects.get(slug=project_name_slug)
    except Project.DoesNotExist:
        project = None

    if request.method == 'POST':
        form = ChangelogForm(request.POST)
        if form.is_valid():
            if project:
                log = form.save(commit=False)
                log.project = project
                log.save()
                return changelog(request, project_name_slug)
            else:
                print form.errors
    else:
        form = ChangelogForm()

    context_dict = {'form': form}

    return render(request, 'changelogs/add_log.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username= username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            invalid_message = "Invalid login details: {} {}".format(username, password)
            print invalid_message
            return HttpResponse(invalid_message)
    else:
        return render(request, 'changelogs/login.html', {})