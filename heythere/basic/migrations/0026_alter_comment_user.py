# Generated by Django 4.0.3 on 2022-07-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0025_rename_name_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
