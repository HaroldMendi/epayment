from django.views.generic import TemplateView, View
from ..models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages


class DashboardView(TemplateView):
    template_name = 'dashboard2.html'

    # def get(self, request, *args, **kwargs):
        
    #     try:
    #         data = Profile.objects.values('mobileofcontactperson').count()
    #         # data2 = Profile.objects.exclude(contactperson__exact='').count()
    #         data2 = Profile.objects.exclude(mobile__isnull=True).count()
    #     except ValueError as e:
    #         data = e

    #     context = {

    #         'data':data,
    #         'data2':data2,
    #     }
    #     return render(self.request, self.template_name, context)
