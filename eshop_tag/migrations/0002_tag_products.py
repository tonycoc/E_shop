# Generated by Django 4.0 on 2022-01-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_alter_product_description'),
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(to='eshop_products.Product'),
        ),
    ]
