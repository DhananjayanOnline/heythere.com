# Generated by Django 4.0.5 on 2022-07-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0058_rename_discription_circle_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='neighbourhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
