from django.db import models
from django.forms import ModelForm
from .models import Resume


class ResumeForm(models.Model):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'phone_number', 'telegram', 'education', 'skills', 'experience', 'projects']
