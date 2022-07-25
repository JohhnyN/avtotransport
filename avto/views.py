from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import *
from django.db.models import Q


def avto(request, *args, **kwargs):
    return HttpResponse('avto')


class AutomobileListView(ListView):
    model = Automobile
    template_name = 'avto/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автотранспорт'
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(car_number__icontains=query) &
                             Q(allowed=True))
        return Automobile.objects.filter(allowed=True)


def create(request):
    today = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    time = datetime.time(23, 59)
    next_day = today + one_day
    date_time = datetime.datetime.combine(today, time)
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.working_shift_id = 1
            response.zone_id = 2
            response.type_id = 2
            response.allowed = True
            response.limitation = date_time
            form.save()
            return redirect('avto')
        else:
            error = 'Форма была неверной'

    form = CreateForm()

    data = {
        'form': form,
        'error': error,
        'title': 'Создание автомобиля'
    }

    return render(request, 'avto/create.html', data)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'avto/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('avto')


def logout_user(request):
    logout(request)
    return redirect('avto')


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'avto/password_change_form.html'


def password_change_done(request):
    return render(request, 'avto/password_change_done.html')




