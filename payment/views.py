from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, View


class LoginPageView(TemplateView):
    template_name= 'login\login.html'