# Generated by Django 2.2.5 on 2019-11-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_candidate_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='dob',
            field=models.DateField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='father_name',
            field=models.TextField(null=True),
        ),
    ]
