# Generated by Django 4.1 on 2022-08-26 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='camada',
            new_name='comision',
        ),
    ]