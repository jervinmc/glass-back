# Generated by Django 4.0.1 on 2023-01-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_rename_recom_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='user_id',
            field=models.IntegerField(default=0.0, verbose_name='user_id'),
        ),
    ]