# Generated by Django 2.2 on 2019-08-27 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190826_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='is_published',
            new_name='is_publish',
        ),
    ]
