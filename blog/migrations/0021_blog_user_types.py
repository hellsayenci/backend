# Generated by Django 2.2 on 2019-09-30 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_auto_20190929_2057'),
        ('blog', '0020_remove_blog_is_public'),
    ]
    
    def migrate_user_types(apps, schema_editor):
        UserType = apps.get_model('users', 'UserType')
        Blog = apps.get_model('blog', 'Blog')
        blogs = Blog.objects.all()
        for e in blogs:
            if e.publisher_profile.user_type is None or e.publisher_profile.user_type.name == 'Undefined' \
                    or e.publisher_profile.user_type.name == 'Public':
                e.user_types.add(UserType.objects.get(name__iexact='Public'))
            elif e.publisher_profile.user_type.name == 'Student':
                e.user_types.add(UserType.objects.get(name__iexact='Student'))
            elif e.publisher_profile.user_type.name == 'Alumni':
                e.user_types.add(UserType.objects.get(name__iexact='Alumni'))
            else:
                e.user_types.add(UserType.objects.get(name__iexact='Public'))

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_types',
            field=models.ManyToManyField(to='users.UserType'),
        ),
        migrations.RunPython(migrate_user_types, reverse_code=migrations.RunPython.noop)
    ]