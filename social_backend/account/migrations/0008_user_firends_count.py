# Generated by Django 5.0.2 on 2024-03-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_create_for_friendshiprequest_created_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firends_count',
            field=models.IntegerField(default=0),
        ),
    ]
