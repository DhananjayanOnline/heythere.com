# Generated by Django 4.0.3 on 2022-06-30 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0022_alter_userregister_neighbourhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.neighbourhood'),
        ),
    ]