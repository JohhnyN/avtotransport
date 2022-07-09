import datetime

from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Select, HiddenInput, ModelChoiceField
from django.forms import modelformset_factory


class CreateForm(ModelForm):

    today = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    time = datetime.time(23, 59)
    next_day = today + one_day
    date_time = datetime.datetime.combine(next_day, time)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].initial = 'NULL'
        self.fields['working_shift'].initial = '1'
        self.fields['zone'].initial = '2'
        self.fields['type'].initial = '2'
        self.fields['limitation'].initial = self.date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.fields['author'].initial = '3'
        self.fields['allowed'].initial = '1'

    class Meta:
        model = Automobile
        car_models = forms.ModelChoiceField(queryset=CarMark.objects.all().filter(car_mark=1))
        fields = '__all__'

        widgets = {
            'organization': Select(attrs={
                'class': 'form-control',
            }),
            'employees': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите сотрудника'
            }),
            'car_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите гос.номер автомобиля'
            }),
            'car_mark': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите марку автомобиля'
            }),
            'car_models': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите модель автомобиля'
            }),
            'car_color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цвет автомобиля'
            }),
            'fio': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фио водителя'
            }),
            'details': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Контактные данные водителя'
            }),
            'position': HiddenInput(),
            'working_shift': HiddenInput(),
            'zone': HiddenInput(),
            'type': HiddenInput(),
            'limitation': HiddenInput(),
            'allowed': HiddenInput(),
            'author': HiddenInput(),
        }


# class CreateAvtoForm(forms.Form):
#     car_mark = forms.ModelChoiceField(queryset=CarMark.objects.all())
    # car_models = forms.ModelChoiceField(queryset=CarModels.objects.all().filter(car_mark=car_mark))

CreateAvtoFormSet = modelformset_factory(
    Automobile, fields=('__all__'), extra=1
)

