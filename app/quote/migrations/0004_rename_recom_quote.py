# Generated by Django 4.0.1 on 2023-01-10 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_rename_quote_recom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recom',
            new_name='Quote',
        ),
    ]
