# Generated by Django 4.0.5 on 2022-06-30 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avto', '0002_alter_carmark_options_alter_carmodels_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='сars',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
