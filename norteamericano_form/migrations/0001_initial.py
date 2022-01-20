# Generated by Django 2.2.24 on 2022-01-19 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NAExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('na_firstname', models.CharField(max_length=100, verbose_name='Nombres')),
                ('na_lastname', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('na_rut', models.CharField(max_length=12, verbose_name='RUT')),
                ('na_birth_date', models.CharField(help_text='Formato DD/MM/AAAA', max_length=10, verbose_name='Fecha Nacimiento')),
                ('na_phone', models.CharField(max_length=30, verbose_name='Teléfono')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]