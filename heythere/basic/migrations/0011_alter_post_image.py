# Generated by Django 4.0.5 on 2022-06-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='x', null=True, upload_to=''),
        ),
    ]
