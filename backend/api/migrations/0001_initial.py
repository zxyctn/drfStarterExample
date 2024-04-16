# Generated by Django 5.0.4 on 2024-04-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Mercedes-Benz', 'mercedes-benz'), ('BMW', 'bmw'), ('Audi', 'audi')], default='mercedes-benz', max_length=15)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]