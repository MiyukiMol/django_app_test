# Generated by Django 4.1.7 on 2023-03-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], max_length=10, null=True),
        ),
    ]
