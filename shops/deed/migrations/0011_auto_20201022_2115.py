# Generated by Django 3.1.2 on 2020-10-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0010_auto_20201022_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default='2020-10-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='income',
            field=models.FloatField(default=00),
            preserve_default=False,
        ),
    ]