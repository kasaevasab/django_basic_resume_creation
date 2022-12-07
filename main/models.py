from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    #title = models.CharField(max_length=200) # TODO: handle similar names of resumes for one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12) # TODO: use a more suitable field or regexp checker
    telegram = models.CharField(max_length=200)
    #avatar = models.ImageField(required=False)
    education = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    projects = models.TextField()


# class Education(models.Model):
#     name = models.CharField(max_length=200)
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#
#
# class Skill(models.Model):
#     name = models.CharField(max_length=200)
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#
#
# class Experience(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#
#
# class Project(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     link = ""
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)