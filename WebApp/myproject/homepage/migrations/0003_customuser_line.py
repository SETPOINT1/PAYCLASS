# Generated by Django 5.1.1 on 2024-12-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_customuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='line',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
