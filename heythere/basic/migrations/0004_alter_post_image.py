# Generated by Django 4.0.5 on 2022-06-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_alter_post_downvote_alter_post_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
