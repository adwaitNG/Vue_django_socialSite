# Generated by Django 5.0.2 on 2024-03-10 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_conversation_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='user',
            new_name='users',
        ),
    ]