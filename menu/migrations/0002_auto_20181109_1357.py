# Generated by Django 2.1.1 on 2018-11-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]