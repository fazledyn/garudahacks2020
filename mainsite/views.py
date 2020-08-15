from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from mainsite.models import Newsletter, Donor, Contact, Assignment, Blog

"""
Render Views
    - home
    - career
    - learning
        - math
        - science
        - law
        - arts
        - life skill
        - webinar
    - foundation
    - blog
    - contact

Form submit Views
    - newsletter
    - donation
    - contact
    - message for us
"""

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def career(request):
    return render(request, 'career.html')

def math(request):
    return render(request, 'maths.html')

def science(request):
    return render(request, 'science.html')

def law(request):
    return render(request, 'law.html')

def arts(request):
    return render(request, 'arts.html')

def life_skill(request):
    return render(request, 'life.html')

def webinar(request):
    return render(request, 'webinar.html')

def foundation(request):
    return render(request, 'foundation.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def riasec(request):
    return render(request, 'riasec.html')

def submission(request):
    return render(request, 'submission.html')

# middle ware post views

def newsletter_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_email = Newsletter(email=email)
        new_email.save()

        return HttpResponseRedirect(reverse('submission'))


def donation_submit(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')

        country = request.POST.get('country')
        email = request.POST.get('email')

        contact_me = request.POST.get('contact_me')

        if contact_me == "on":
            contact_me = True
        else:
            contact_me = False

        donor = Donor(  email=email, 
                        first_name=first_name, 
                        last_name=last_name,
                        country=country,
                        contact_me=contact_me
                    )
        donor.save()
        return HttpResponseRedirect(reverse('submission'))


def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        comment = request.POST.get('comment')

        contact = Contact(  name=name,
                            username=username,
                            comment=comment
                        )
        contact.save()
        return HttpResponseRedirect(reverse('submission'))


def assignment_submit(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        assignment = Assignment(file=file)
        assignment.save()

        return HttpResponseRedirect(reverse('submission'))


def blog_submission(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        blog = Blog(file=file)
        blog.save()

        return HttpResponseRedirect(reverse('submission'))