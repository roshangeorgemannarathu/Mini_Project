# Generated by Django 3.2.20 on 2023-11-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aapmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aquarium',
            name='description',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_breed',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_description',
            field=models.TextField(max_length=30, null=True),
        ),
    ]