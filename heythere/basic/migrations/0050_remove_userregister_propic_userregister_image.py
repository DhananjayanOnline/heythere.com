# Generated by Django 4.0.5 on 2022-07-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0049_alter_post_image_alter_userregister_propic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='propic',
        ),
        migrations.AddField(
            model_name='userregister',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]