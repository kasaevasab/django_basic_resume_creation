from django.db import models
from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'email', 'phone_number', 'telegram',
                  'education', 'skills', 'experience', 'projects']
