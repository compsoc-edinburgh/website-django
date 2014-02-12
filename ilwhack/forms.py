import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
# ILWHack forms
from ilwhack.models import Participant, Project, Team

class MatricField(forms.CharField):
    def __init__(self, **kwargs):
        forms.CharField.__init__(self, **kwargs)
    
    def clean(self, value):
        if re.search(r'^\s*[sS]?\d{7}\s*$', value) is not None:
            return super(MatricField, self).clean(value)
        else:
            raise forms.ValidationError, "Matric numbers should be in the format 's1234567'"
        

class RegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=200)
    real_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    matric_no = MatricField(max_length=8)
    department = forms.CharField(max_length=100, help_text='E.g. Informatics, Business, Design, etc.')
    bio = forms.CharField(widget=forms.Textarea, required=False)
    captcha = CaptchaField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['display_name', 'real_name', 'department', 'bio']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project


class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']