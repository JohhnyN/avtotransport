from django.db import models
from django.contrib.auth.models import User


class CarMark(models.Model):
    car_mark = models.CharField(max_length=20, unique=True, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.car_mark

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class CarModels(models.Model):
    car_models = models.CharField(max_length=40, verbose_name='модель автомобиля')
    car_mark = models.ForeignKey('CarMark', on_delete=models.PROTECT, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.car_models

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'


class WorkingShift(models.Model):
    working_shift = models.CharField(max_length=20, verbose_name='Смена')

    def __str__(self):
        return self.working_shift

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'


class Zone(models.Model):
    zone = models.CharField(max_length=20, verbose_name='Зона')

    def __str__(self):
        return self.zone

    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'


class Type(models.Model):
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['type']


class Organization(models.Model):
    organization = models.CharField(max_length=255, unique=True, verbose_name='Организация')

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['organization']


class Employees(models.Model):
    employees = models.CharField(max_length=255, verbose_name='Сотрудник')
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT, verbose_name='Организация')
    position = models.CharField(max_length=255, verbose_name='Должность сотрудника')
    details = models.CharField(max_length=255, verbose_name='Контактные данные')

    def __str__(self):
        return self.employees

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Automobile(models.Model):
    car_number = models.CharField(max_length=10, unique=True, verbose_name='№ автомобиля')
    car_mark = models.ForeignKey('CarMark', on_delete=models.PROTECT, verbose_name='Марка автомобиля')
    car_models = models.ForeignKey('CarModels', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    car_color = models.CharField(max_length=15, verbose_name='Цвет автомобиля')
    fio = models.CharField(max_length=255, verbose_name='ФИО владельца')
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT, verbose_name='Организация')
    position = models.CharField(max_length=255, verbose_name='Должность владельца', null=True)
    details = models.CharField(max_length=255, verbose_name='Контактные данные')
    working_shift = models.ForeignKey('WorkingShift', on_delete=models.PROTECT, verbose_name='Смена')
    zone = models.ForeignKey('Zone', on_delete=models.PROTECT, verbose_name='Зона')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип')
    limitation = models.DateTimeField(verbose_name='Срок')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT, default='auth.User', verbose_name='Пользователь')
    employees = models.ForeignKey('employees', on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')
    allowed = models.BooleanField(default=True, verbose_name='Разрешено')

    def __str__(self):
        return self.car_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['car_number']

