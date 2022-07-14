from django.contrib import admin
from .models import *


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_mark',)
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
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    search_fields = ('type',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization',)
    list_display_links = ('organization',)
    search_fields = ('organization',)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employees', 'organization', 'position', 'details')
    list_display_links = ('organization',)
    search_fields = ('employees',)


@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_number', 'car_mark', 'fio', 'organization', 'working_shift', 'zone', 'type', 'limitation', 'author', 'allowed')
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
