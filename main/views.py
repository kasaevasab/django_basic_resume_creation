from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from main.models import Resume


def home_view(request):
    return render(request, "main/home.html")


@login_required(login_url='login')
def display_resume(request):
    print(request.user)
    resume = Resume.objects.get(user=request.user)
    p = request.POST
    if request.method == "POST":
        save_resume(request, resume)
        if p.get('export_pdf'):
            pass
    return render(request, "main/resume.html", {"resume": resume})


def save_resume(request, resume):
    p = request.POST
    resume.name = p.get("name")
    resume.surname = p.get("surname")
    resume.phone_number = p.get("phone_number")
    resume.telegram = p.get("telegram")
    resume.education = p.get("education")
    resume.skills = p.get("skills")
    resume.experience = p.get("experience")
    resume.projects = p.get("projects")
    resume.save()
    return