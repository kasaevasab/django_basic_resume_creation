from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    # title = models.CharField(max_length=200) # TODO: handle similar names of resumes for one user

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='static/images', default='./static/images/default-avatar.png')
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=12, default='')  # TODO: use a more suitable field or regexp checker
    telegram = models.CharField(max_length=200, default='')
    education = models.TextField(default=' ')
    skills = models.TextField(default=' ')
    experience = models.TextField(default=' ')
    projects = models.TextField(default=' ')

    def save(self, *args, **kwargs):
        print('save() is called.')
        super(Resume, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + self.surname + " resume"

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
