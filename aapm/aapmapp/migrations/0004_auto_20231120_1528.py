# Generated by Django 3.2.20 on 2023-11-20 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aapmapp', '0003_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(max_length=255)),
                ('item_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aapmapp.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]