# Generated by Django 4.0.5 on 2022-07-05 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0042_post_global_visibility_post_local_visibility_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_create']},
        ),
    ]
