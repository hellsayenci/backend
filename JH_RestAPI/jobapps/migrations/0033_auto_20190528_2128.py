# Generated by Django 2.2 on 2019-05-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0032_auto_20190528_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]