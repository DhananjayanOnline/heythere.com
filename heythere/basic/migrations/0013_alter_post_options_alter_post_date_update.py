# Generated by Django 4.0.3 on 2022-06-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_update', '-date_create']},
        ),
        migrations.AlterField(
            model_name='post',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
