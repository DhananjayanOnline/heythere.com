# Generated by Django 4.0.5 on 2022-07-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0039_remove_userregister_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='neighbourhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
