# Generated by Django 2.1 on 2019-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_name', models.CharField(max_length=20)),
                ('Class', models.CharField(help_text='Type number between 1 to 10', max_length=5)),
                ('Divition', models.CharField(help_text='Type A or B or C', max_length=5)),
                ('Mob_no', models.CharField(max_length=10)),
                ('Address', models.TextField(max_length=100)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
