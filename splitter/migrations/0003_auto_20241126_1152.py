# Generated by Django 3.0.5 on 2024-11-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
