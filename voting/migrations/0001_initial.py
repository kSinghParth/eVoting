# Generated by Django 2.2.5 on 2019-09-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.IntegerField()),
                ('candidate', models.IntegerField()),
            ],
        ),
    ]
