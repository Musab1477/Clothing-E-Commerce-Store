# Generated by Django 5.0.1 on 2024-07-13 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_signupdetail_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signUpDetail',
        ),
    ]
