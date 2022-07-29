from django.apps import AppConfig
import datetime


class AvtoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avto'
    verbose_name = 'Автотранспорт'