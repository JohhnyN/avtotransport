from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *


def avto(request, *args, **kwargs):
    return HttpResponse('avto')


class AvtoListView(ListView):
    model = Сars
    template_name = 'avto/index.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Сars.objects.filter(allowed=True)

