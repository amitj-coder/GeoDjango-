# Generated by Django 3.1.2 on 2020-10-24 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0013_auto_20201024_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesDeedRepresentative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative_name', models.CharField(max_length=200)),
                ('representative_married', models.BooleanField(default=False)),
                ('representative_fwm_name', models.CharField(max_length=150)),
                ('representative_birth_date', models.DateField()),
                ('representative_occupation', models.CharField(max_length=150)),
                ('representative_address', models.TextField()),
                ('representative_seller', models.BooleanField(default=False)),
                ('representative_unique_id', models.CharField(max_length=150)),
                ('representative_fwm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deed.fmw')),
                ('representative_gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deed.gender')),
            ],
        ),
    ]