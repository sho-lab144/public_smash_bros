# Generated by Django 4.2.19 on 2025-03-03 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0005_alter_match_id"),
    ]

    operations = [
        migrations.RenameField(model_name="match", old_name="id", new_name="match_id",),
    ]
