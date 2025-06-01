from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import House
from .forms import HouseCreateForm
from django.views.generic import ListView
from django.contrib import messages
from mixin.mixin import LoginRequired
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

class HouseListView(LoginRequired, ListView):
    template_name = 'page/house/house-list.html'

    def get(self, request, *args, **kwargs):
        data = House.objects.order_by('-created_at')
        paginator = Paginator(data , 5)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        data = {
            'page_obj': page
        }
        if 'search' in request.GET:
            search = request.GET.get('search', '')
            search_data = House.objects.filter(
                Q(owner__fname__icontains=search) |
                Q(owner__lname__icontains=search) |
                Q(block_number__icontains=search)).order_by('-created_at')
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


class HouseCreateView(LoginRequired):

    template_name = 'page/house/house-create.html'

    def get(self, request, *args, **kwargs):
        form = HouseCreateForm()
        context = {
            'form': form,
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = HouseCreateForm(request.POST)

        block = request.POST.get('block_number')
        lot = request.POST.get('lot_number')

        try:
            if House.objects.filter(block_number=block,lot_number=lot).exists():
                messages.error(request, 'Block and Lot number already in used!')
            elif form.is_valid():
                data = form.save(commit=False)
                data.created_by = self.request.user
                form.save()
                form = HouseCreateForm()
                messages.success(request, 'House information successfully created!')
        except ValueError:
            messages.error(request, 'Block and lot field should be number and not empty.')

        context = {
            'form':form,
        }
        return render(self.request, self.template_name, context)
