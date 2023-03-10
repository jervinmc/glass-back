# Generated by Django 4.0.1 on 2022-12-20 11:41

from django.db import migrations, models
import product.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.IntegerField(default=0.0, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='price')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='product_name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('image', models.ImageField(default='uploads/users_placeholder.png', upload_to=product.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
