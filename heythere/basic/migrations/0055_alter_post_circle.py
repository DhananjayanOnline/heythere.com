# Generated by Django 4.0.5 on 2022-07-14 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0054_remove_post_circle_visibility_alter_post_circle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='circle',
            field=models.ForeignKey(blank=True, default='x', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='circle', to='basic.circle'),
        ),
    ]
