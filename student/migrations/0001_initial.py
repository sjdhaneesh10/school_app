# Generated by Django 2.1 on 2019-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Divition', models.CharField(max_length=5)),
                ('Teacher_Name', models.CharField(max_length=20)),
                ('Address', models.TextField(max_length=100)),
                ('DOB', models.DateField(max_length=8)),
            ],
        ),
    ]
