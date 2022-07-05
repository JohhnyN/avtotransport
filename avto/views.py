from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import *


def avto(request, *args, **kwargs):
    return HttpResponse('avto')


class AutomobileListView(ListView):
    model = Automobile
    template_name = 'avto/index.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Automobile.objects.filter(allowed=True)


def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            form.save()
        else:
            error = 'Форма была неверной'
            print(form)

    form = CreateForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'avto/create.html', data)




