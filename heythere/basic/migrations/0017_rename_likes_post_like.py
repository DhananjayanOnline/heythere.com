# Generated by Django 4.0.5 on 2022-06-29 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_remove_post_like_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='like',
        ),
    ]
