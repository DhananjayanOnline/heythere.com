# Generated by Django 4.0.5 on 2022-06-29 15:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic', '0014_remove_post_downvote_remove_post_upvote_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
