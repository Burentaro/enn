# Generated by Django 2.1.1 on 2018-11-13 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
