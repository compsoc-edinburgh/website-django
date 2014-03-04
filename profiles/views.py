from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from profiles.models import Profile, Skill, ExternalPlace

@login_required
def view(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    skills = Skill.objects.filter(profile=profile)
    external_places = ExternalPlace.objects.filter(profile=profile)

    data = {
        'user': user,
        'profile': profile,
        'skills': skills,
        'external_places': external_places,
    }

    return render_to_response('profiles/view.html', data)