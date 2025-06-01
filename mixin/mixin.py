from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic import View, RedirectView


def has_group(user, group_name):
    
    try:
        group_name = Group.objects.get(name=group_name)
        return True if group_name in user.groups.all() else False
    except Group.DoesNotExist:
        return False
    
    
class EditorMixin(View):
    def dispatch(self, request, *args, **kwargs):
        redirect_page = redirect('login')
        if request.user.is_authenticated and has_group(request.user, 'editor') \
            or request.user.is_superuser:
            redirect_page = super(EditorMixin, self).dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:
            return redirect('access_denied')
        return redirect_page
    
class ViewerMixin(View):
    def dispatch(self, request, *args, **kwargs):
        redirect_page = redirect('login')
        if request.user.is_authenticated and has_group(request.user, 'viewer') \
            or request.user.is_superuser:
            redirect_page = super(ViewerMixin, self).dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:
            return redirect('access_denied')
        return redirect_page
    
class LoginRequired(View):
    def dispatch(self, request, *args, **kwargs):
        redirect_page = redirect('login')
        if request.user.is_authenticated or request.user.is_superuser:
            redirect_page = super(LoginRequired, self).dispatch(request, *args, **kwargs)
        return redirect_page