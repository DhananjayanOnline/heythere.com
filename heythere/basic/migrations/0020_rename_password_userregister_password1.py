# Generated by Django 4.0.3 on 2022-06-30 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0019_rename_like_post_likes_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='password',
            new_name='password1',
        ),
    ]