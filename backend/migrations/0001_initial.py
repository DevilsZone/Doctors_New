# Generated by Django 3.0.8 on 2020-07-01 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_name', models.TextField()),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=30)),
                ('speciality', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=20)),
                ('long', models.CharField(max_length=20)),
                ('distance', models.CharField(max_length=20)),
                ('doctors', models.TextField()),
                ('relation_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ZipCode')),
            ],
        ),
    ]