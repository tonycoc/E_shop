# Generated by Django 4.0 on 2022-01-14 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_tag', '0004_remove_ex_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='ex',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_tag.tag'),
        ),
    ]