# Generated by Django 3.1.2 on 2020-10-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender1',
        ),
    ]
