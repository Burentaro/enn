# Generated by Django 2.1.1 on 2018-11-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20181113_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
