# Generated by Django 3.1.3 on 2020-11-06 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxquote', '0003_auto_20201106_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpc',
            name='licencias_mpc',
            field=models.ManyToManyField(blank=True, help_text='Seleccione las posibles licencias', to='mxquote.Licencias'),
        ),
    ]
