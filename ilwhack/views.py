from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User
from ilwhack.models import Page, Participant, Team, Project
from ilwhack.forms import RegisterForm, ProfileForm, ProjectForm, CreateTeamForm


def get_nav_pages():
    return Page.objects.filter(is_in_navbar__exact=True).values('name', 'nav_name')


def get_base_context():
    return { 'nav_pages': get_nav_pages() }


class PageView(TemplateView):
    template_name = 'ilwhack/page.html'
    
    def get(self, request, page_name):
        context = get_base_context()
        context['page'] = get_object_or_404(Page, name = page_name)
        return render(request, self.template_name,  context)


class RegisterView(TemplateView):
    template_name = 'ilwhack/register.html'
    
    def get(self, request):
        context = get_base_context()
        context['form'] = RegisterForm
        return render(request, self.template_name, { 'form': RegisterForm(), 'nav_pages': get_nav_pages() })
    
    def post(self, request):
        form = RegisterForm(request.POST)
        context = get_base_context()
        context['form'] = form
        
        if form.is_valid():
            # Register our new user! :D
            newuser = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1']
            )
            Participant.objects.create(
                user=newuser,
                display_name=form.cleaned_data['display_name'],
                real_name=form.cleaned_data['real_name'],
                matric_no=form.cleaned_data['matric_no'],
                bio=form.cleaned_data['bio'],
                department = form.cleaned_data['department']
            )
            
            return HttpResponseRedirect('/ilwhack/login/')
        
        else:
            return render(request, self.template_name, context)


@login_required
def myprofile(request):
    context = get_base_context()
    participant = Participant.objects.get(user = request.user)
    form = ProfileForm(instance=participant)
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
    
    context['form'] = form
    return render(request, 'ilwhack/myprofile.html', context)


@login_required
def myaccount(request):
    return render(request, 'ilwhack/myaccount.html', get_base_context())


@login_required
def myteam(request):
    if request.method == 'POST':
        if not request.user.participant.team.project:
            request.user.participant.team.project = Project.objects.create(
                name='' + request.user.participant.team.name + "'s Project"
            )
            request.user.participant.team.save()
        
        form = ProjectForm(request.POST, instance=request.user.participant.team.project)
        form.save()
        context = get_base_context()
        context['form'] = form
        return render(request, 'ilwhack/myteam.html', context)
        
    else:
        context = get_base_context()
        context['form'] = ProjectForm()
        return render(request, 'ilwhack/myteam.html', context)


@login_required
def myteam_leave(request):
    request.user.participant.leave_team()
    return HttpResponseRedirect('/ilwhack/myteam/')


@login_required
def myteam_join(request, which):
    request.user.participant.team = Team.objects.get(id=which)
    request.user.participant.save()
    return HttpResponseRedirect('/ilwhack/myteam/')


def check_not_in_team(user):
    return not user.participant.team


@login_required
@user_passes_test(check_not_in_team)
def myteam_create(request):
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data['name']
            userp = request.user.participant
            team = Team.objects.create(name = team_name)
            team.save()
            userp.team = team
            userp.is_leader = True
            userp.save()
    return HttpResponseRedirect('/ilwhack/myteam/')


def check_is_leader(user):
    return (True and user.participant.team and user.participant.is_leader)

def check_is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(check_is_leader)
def myteam_makeleader(request, who):
    request.user.participant.give_leader_to(User.objects.get(id=who).participant)
    return HttpResponseRedirect('/ilwhack/myteam/')    

@login_required
@user_passes_test(check_is_leader)
def project(request):
    """Enable a team leader to Update (or create) their team's project."""
    if request.method == 'POST':
        
        def _get_project(participant):
            if participant.team.project:
                return participant.team.project
            else:
                project = Project.objects.create(name='A Project', pitch='')
                participant.team.project = project
                participant.team.save()
                return project
        
        form = ProjectForm(request.POST, instance=_get_project(request.user.participant))
        
        if form.is_valid():
            form.save()
        
        context = get_base_context()
        context["form"] = form
        return render(request, 'ilwhack/project.html', context)
        
    else:
        
        form = ProjectForm(instance=request.user.participant.team.project)
        
        context = get_base_context()
        context["form"] = form
        return render(request, 'ilwhack/project.html', context)


@login_required
@user_passes_test(check_is_staff)
def participants(request):
    """Display a list of participants, for staff use."""
    context = get_base_context()
    context['participants'] = Participant.objects.all()
    context['emails'] = ', '.join(set([ user['email'] for user in User.objects.filter(participant__isnull=False).values('email') ]))
    return render(request, 'ilwhack/participants.html', context)


def teams(request):
    context = get_base_context()
    context['teams'] = Team.objects.all()
    context['participants'] = Participant.objects.all()
    return render(request, 'ilwhack/teams.html', context)