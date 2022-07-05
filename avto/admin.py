from django.contrib import admin
from .models import *


class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('car_mark',)
    list_display_links = ('car_mark',)
    search_fields = ('car_mark',)


class CarModelsAdmin(admin.ModelAdmin):
    list_display = ('car_models', 'car_mark')
    list_display_links = ('car_models', 'car_mark')


class WorkingShiftAdmin(admin.ModelAdmin):
    list_display = ('working_shift',)
    list_display_links = ('working_shift',)
    search_fields = ('working_shift',)


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('zone',)
    list_display_links = ('zone',)
    search_fields = ('zone',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    search_fields = ('type',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization',)
    list_display_links = ('organization',)
    search_fields = ('organization',)


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employees', 'organization', 'position', 'details')
    list_display_links = ('organization',)
    search_fields = ('organization',)


class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'car_mark', 'car_models', 'fio', 'organization', 'working_shift', 'zone', 'type', 'limitation', 'author', 'allowed')
    list_display_links = ('car_number',)
    list_editable = ('allowed',)
    search_fields = ('car_number', 'fio')
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    # def get_form(self, request, *args, **kwargs):
    #     form = super(CarsAdmin, self).get_form(request, *args, **kwargs)
    #     form.base_fields['author'].initial = request.user
    #     return form


admin.site.register(CarMark, CarMarkAdmin)
admin.site.register(CarModels, CarModelsAdmin)
admin.site.register(WorkingShift, WorkingShiftAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Automobile, AutomobileAdmin)
