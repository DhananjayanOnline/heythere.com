# Generated by Django 4.0.5 on 2022-07-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_room_options_room_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='neighbourhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
