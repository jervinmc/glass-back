# Generated by Django 4.0.1 on 2022-12-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='size'),
        ),
    ]
