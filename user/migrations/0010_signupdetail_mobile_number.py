# Generated by Django 5.0.6 on 2024-07-14 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_signupdetail_email_alter_signupdetail_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupdetail',
            name='mobile_number',
            field=models.CharField(default='+1234567890', max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
