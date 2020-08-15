from django.urls import path
from cotter import views

urlpatterns = [
    path('/login',  views.login, name='cotter-login'),
]