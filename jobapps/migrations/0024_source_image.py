# Generated by Django 2.2 on 2019-04-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobapps', '0023_sourcetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]