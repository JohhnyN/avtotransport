import tablib
from django.contrib import admin
from import_export import resources
from django.apps import apps
from import_export.admin import ImportExportModelAdmin

from .models import *


class EmployyesResourse(resources.ModelResource):
    class Meta:
        model = Employees
        fields = ('organization__organization', 'employees',  'position', 'details', 'note', 'rental_period')


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('car_mark',)
    list_display_links = ('car_mark',)
    search_fields = ('car_mark',)


@admin.register(WorkingShift)
class WorkingShiftAdmin(admin.ModelAdmin):
    list_display = ('working_shift',)
    list_display_links = ('working_shift',)
    search_fields = ('working_shift',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('zone',)
    list_display_links = ('zone',)
    search_fields = ('zone',)


@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    search_fields = ('type',)


@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('organization', 'rental_period')
    list_display_links = ('organization',)
    search_fields = ('organization',)


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('employees', 'organization', 'position', 'details', 'rental_period')
    list_display_links = ('employees', 'organization',)
    search_fields = ('employees',)
    resource_class = EmployyesResourse


@admin.register(Automobile)
class AutomobileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('car_number', 'car_mark', 'fio', 'organization', 'working_shift', 'zone', 'type', 'limitation', 'author', 'allowed')
    list_display_links = ('car_number',)
    list_editable = ('allowed',)
    search_fields = ('car_number', 'fio',)
    exclude = ('author',)
    list_select_related = ['car_mark', 'organization']
    # raw_id_fields = ['organization']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# admin.site.register(CarMark, CarMarkAdmin)
# admin.site.register(WorkingShift, WorkingShiftAdmin)
# admin.site.register(Zone, ZoneAdmin)
# admin.site.register(Type, TypeAdmin)
# admin.site.register(Organization, OrganizationAdmin)
# admin.site.register(Employees, EmployeesAdmin)
# admin.site.register(Automobile, AutomobileAdmin)
