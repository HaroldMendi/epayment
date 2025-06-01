from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from ..forms.users import UserCreateForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User




class UserCreateView(View):
    template_name = 'login/register.html'

    def get(self, requests, *args, **kwargs):
        form = UserCreateForm()
        context = {
            'form':form
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Account was created for ' + user)
            # return redirect('login')
            form = UserCreateForm()
        context = {
            'form':form
        }
        return render(self.request, self.template_name, context)
    
class LoginView(View):

    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            'form': form   
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect.')
        context = {
            'form':form
        }
        return render(self.request, self.template_name, context)
    
def Logout(request):
    logout(request)
    messages.success(request, 'Successfull logged out!')
    return redirect('home')

def check_username(request):
    username = request.POST.get('username')
    if User.objects.filter(username=username).exists():
        return HttpResponse('Username already exists')
    else:
        return HttpResponse('Username is available')