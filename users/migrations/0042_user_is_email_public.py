# Generated by Django 2.2 on 2019-09-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_feedback_from_demo_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_public',
            field=models.BooleanField(default=True),
        ),
    ]