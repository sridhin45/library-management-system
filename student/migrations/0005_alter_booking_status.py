# Generated by Django 5.1.1 on 2024-10-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
