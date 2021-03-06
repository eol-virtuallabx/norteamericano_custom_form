# Generated by Django 2.2.24 on 2022-01-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norteamericano_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naextrainfo',
            name='na_firstname',
        ),
        migrations.RemoveField(
            model_name='naextrainfo',
            name='na_lastname',
        ),
        migrations.AddField(
            model_name='naextrainfo',
            name='na_lastname_m',
            field=models.CharField(default='', max_length=100, verbose_name='Apellido Materno'),
        ),
        migrations.AddField(
            model_name='naextrainfo',
            name='na_lastname_p',
            field=models.CharField(default='', max_length=100, verbose_name='Apellido Paterno'),
        ),
        migrations.AddField(
            model_name='naextrainfo',
            name='na_names',
            field=models.CharField(default='', max_length=100, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='naextrainfo',
            name='na_birth_date',
            field=models.CharField(default='', help_text='Formato DD/MM/AAAA', max_length=10, verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='naextrainfo',
            name='na_phone',
            field=models.CharField(default='', max_length=30, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='naextrainfo',
            name='na_rut',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='RUT'),
        ),
    ]
