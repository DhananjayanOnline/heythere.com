# Generated by Django 4.0.5 on 2022-07-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_activeusers_options_activeusers_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
