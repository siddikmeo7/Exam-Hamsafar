# Generated by Django 5.0 on 2024-11-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamsafar', '0003_booktrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktrip',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]