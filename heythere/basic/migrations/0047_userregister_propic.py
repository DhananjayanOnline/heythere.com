# Generated by Django 4.0.5 on 2022-07-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0046_userregister_fname_userregister_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='propic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]