# Generated by Django 2.1.1 on 2018-11-05 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('Drink', 'Drink'), ('Food', 'Food')], max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
