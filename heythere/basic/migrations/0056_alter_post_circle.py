# Generated by Django 4.0.5 on 2022-07-14 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0055_alter_post_circle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='circle',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='circle', to='basic.circle'),
        ),
    ]
