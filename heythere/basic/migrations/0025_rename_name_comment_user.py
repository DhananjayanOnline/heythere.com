# Generated by Django 4.0.3 on 2022-07-01 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0024_comment_delete_votestatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]
