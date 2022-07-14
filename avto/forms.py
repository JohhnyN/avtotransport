import datetime

from django.contrib.auth.forms import AuthenticationForm

from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Select, HiddenInput, ModelChoiceField


class CreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Automobile
        fields = 'car_number', 'car_mark', 'car_color', 'fio', 'details', 'organization', 'employees'

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
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

