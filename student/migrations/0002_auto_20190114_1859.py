# Generated by Django 2.1 on 2019-01-14 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Divition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divition.Divition'),
        ),
    ]
