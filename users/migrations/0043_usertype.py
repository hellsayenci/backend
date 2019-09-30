# Generated by Django 2.2 on 2019-09-28 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_user_is_email_public'),
    ]

    def create_user_types(apps, schema_editor):
        UserType = apps.get_model('users', 'UserType')
        User = apps.get_model('users', 'User')
        undefined = UserType(name='Undefined')
        undefined.save()
        public = UserType(name='Public')
        public.save()
        student = UserType(name='Student')
        student.save()
        alumni = UserType(name='Alumni')
        alumni.save()

        users = User.objects.all()
        for user in users:
            if user.user_type == 0:
                user.type = undefined
            elif user.user_type == 1:
                user.type = public
            elif user.user_type == 2:
                user.type = student
            elif user.user_type == 3:
                user.type = alumni
            user.save()

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.UserType'),
        ),
        migrations.RunPython(create_user_types, reverse_code=migrations.RunPython.noop)
    ]