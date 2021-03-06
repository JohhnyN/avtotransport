from django.db import models
from django.contrib.auth.models import User


class CarMark(models.Model):
    car_mark = models.CharField(max_length=20, unique=True, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.car_mark

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'
        ordering = ['car_mark']


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
    rental_period = models.DateTimeField(verbose_name='Срок аренды', blank=True, null=True)

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['organization']


class Employees(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name='Организация', related_name='employees')
    employees = models.CharField(max_length=255, verbose_name='Сотрудник')
    position = models.CharField(max_length=255, verbose_name='Должность сотрудника')
    details = models.CharField(max_length=255, verbose_name='Контактные данные')
    note = models.TextField(blank=True, verbose_name='Примечание')
    rental_period = models.DateTimeField(verbose_name='Срок аренды', blank=True, null=True)

    def __str__(self):
        return self.employees

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Automobile(models.Model):
    car_number = models.CharField(max_length=10, unique=True, verbose_name='№ автомобиля')
    car_mark = models.ForeignKey('CarMark', on_delete=models.PROTECT, verbose_name='Марка автомобиля', related_name='car_number')
    car_color = models.CharField(max_length=15, verbose_name='Цвет автомобиля')
    fio = models.CharField(max_length=255, verbose_name='ФИО владельца')
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT, verbose_name='Организация', related_name='car_number')
    position = models.CharField(max_length=255, verbose_name='Должность владельца', null=True)
    details = models.CharField(max_length=255, verbose_name='Контактные данные')
    working_shift = models.ForeignKey('WorkingShift', on_delete=models.PROTECT, verbose_name='Смена')
    zone = models.ForeignKey('Zone', on_delete=models.PROTECT, verbose_name='Зона')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип')
    limitation = models.DateTimeField(verbose_name='Срок')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT, default='auth.User', verbose_name='Пользователь')
    employees = models.ForeignKey('employees', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник', related_name='car_number')
    allowed = models.BooleanField(default=True, verbose_name='Разрешено')
    note = models.TextField(blank=True, verbose_name='Примечание')

    def __str__(self):
        return self.car_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
