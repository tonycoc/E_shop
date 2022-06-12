# Generated by Django 4.0 on 2022-06-06 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('eshop_account', '0003_alter_reset_code_reset_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reset_password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_code', models.IntegerField(null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name': 'کد بازگردانی رمز عبور',
                'verbose_name_plural': 'کد های بازگردانی رمز عبور',
            },
        ),
        migrations.DeleteModel(
            name='Reset_code',
        ),
    ]