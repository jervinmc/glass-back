# Generated by Django 4.0.1 on 2023-01-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='status'),
        ),
    ]
