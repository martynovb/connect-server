# Generated by Django 4.2.4 on 2023-08-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_businessprofile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='updated',
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='title',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
