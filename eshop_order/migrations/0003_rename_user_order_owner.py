# Generated by Django 4.0 on 2022-01-25 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0002_alter_order_add_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='owner',
        ),
    ]
