# Generated by Django 2.2.5 on 2019-11-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20191120_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
