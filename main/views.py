from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resume
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


@login_required(login_url='login')
def resume_view(request):
    print(request.user)
    try:
        resume = Resume.objects.get(user=request.user)
    except:
        resume = request.user.resume_set.create()
    if request.method == 'POST':
        p = request.POST
        print(request.POST)

        # да простят меня Боги программирования за это полотно..........
        # (там честно было более изящное решение через формы, но там кастомизация некрасивая выходила((((((((((

        resume.name = p['name']
        resume.surname = p['surname']
        resume.email = p['email']
        resume.phone_number = p['phone_number']
        resume.telegram = p['telegram']
        resume.education = p['education']
        resume.skills = p['skills']
        resume.experience = p['experience']
        resume.projects = p['projects']
        resume.save()
        resume = Resume.objects.get(user=request.user)
        # resume.avatar = p['avatar']

        if 'export_pdf' in p:
            return FileResponse(resume_to_pdf(resume), as_attachment=True, filename='resume.pdf')
    return render(request, 'main/resume.html', {'resume': resume})


def resume_to_pdf(resume):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text = c.beginText()
    text.setTextOrigin(inch, inch)
    text.setFont('Helvetica', 14)

    lines = ["Name: " + resume.name, "Surname: " + resume.surname, "Email: " + resume.email,
             "Phone Number: " + resume.phone_number, "Telegram: " + resume.telegram]

    for line in lines:
        text.textLine(line)

    text.textLines("Education:\n" + resume.education.strip())
    text.textLines("Skills:\n" + resume.skills.strip())
    text.textLines("Experience:\n" + resume.experience.strip())
    text.textLines("Projects:\n" + resume.projects.strip())

    c.drawText(text)
    c.showPage()
    c.save()
    buf.seek(0)

    return buf
