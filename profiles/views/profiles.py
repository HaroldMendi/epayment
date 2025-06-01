from django.shortcuts import render, redirect, get_object_or_404
from ..models import Profile
from ..forms.profiles import ProfileCreateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import TemplateView
import datetime
from mixin.mixin import EditorMixin, ViewerMixin, LoginRequired
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.

class AccessDeniedView(TemplateView):
    template_name = 'page/profile/access-denied.html'

class ProfileListView(LoginRequired):
    template_name = 'page/profile/profile-list.html'

    def get(self, request, *args, **kwargs):
        data = Profile.objects.order_by('-created_at')
        paginator = Paginator(data, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'page_obj': page_obj,
        }
        if 'search' in request.GET:
            search = request.GET.get('search', '')
            search_data = Profile.objects.filter(
                Q(fname__icontains=search)|
                Q(lname__icontains=search)).order_by('-created_at')
            p = Paginator(search_data, 5)
            page_num = request.GET.get('page', 1)

            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(1)
            context = { 'page_obj': page, 'search':search }
            return render(self.request, self.template_name, context)
        else: 
            return render(self.request, self.template_name, data)   

class ProfileCreationForm(EditorMixin):
    template_name = 'page/profile/profile-create.html'

    def get(self, request, *args, **kwargs):
        form = ProfileCreateForm()
        context = {
            'form' : form
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(request.POST)
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        try:
            if Profile.objects.filter(fname=f_name, lname=l_name).exists():
                messages.error(request, 'Firstname and lastname exists in database!')
            elif form.is_valid():
                data = form.save(commit=False)
                data.created_by = self.request.user
                form.save()
                form = ProfileCreateForm()
                messages.success(request, f'Successfuly created profile for {f_name} {l_name}')
        except ValueError:
            messages.error(request, 'ERROR')

        context = {
            'form' : form,
        }
        return render(self.request, self.template_name, context)

class ProfileDetailView(ViewerMixin):

    template_name = 'page/profile/profile-detail.html'

    def get(self, request, *args,**kwargs):
        data = get_object_or_404(Profile, slug=self.kwargs['slug'])
        context = {
            'data': data,
        }
        return render(self.request, self.template_name, context)
   
class ProfileUpdateView(EditorMixin):
    template_name = 'page/profile/profile-update.html'

    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form = ProfileUpdateForm(instance=data)
        context = {
            'form': form,
            'data': data
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        data = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form = ProfileUpdateForm(request.POST or None ,instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.updated_by = self.request.user
            data.updated_at = datetime.datetime.now()
            form.save()
            messages.success(request, 'Updated Successfuly!')
            return JsonResponse({'success': True})
        context = {
            'form':form,
            'data':data
        }
        return render(self.request, self.template_name, context)

