from django.urls import path
from mainsite import views

urlpatterns = [
    path('',       views.index,    name='index'),
    path('home/',   views.home,    name='home'),
    path('career/', views.career,    name='career'),

    path('math/',       views.math,    name='math'),
    path('science/',       views.science,    name='science'),
    path('law/',       views.law,    name='law'),
    path('arts/',       views.arts,    name='arts'),
    path('life/',       views.life_skill,    name='life-skill'),
    path('webinar/',       views.webinar,    name='webinar'),

    path('foundation/',       views.foundation,    name='foundation'),
    path('blog/',       views.blog,    name='blog'),
    path('contact/',       views.contact,    name='contact'),
    path('riasec/',       views.riasec,    name='riasec'),
    path('submission/',      views.submission,   name='submission'),

    path('newsletter_submit/',       views.newsletter_submit,    name='newsletter'),
    path('donation_submit/',       views.donation_submit,    name='donation'),
    path('assignment_submit/',      views.assignment_submit,    name='assignment'),
    path('blog_submit/',        views.blog_submission, name='blog-submit'),
    path('contact_submit/',     views.contact_submit, name='contact-submit'),
]