# Generated by Django 4.2.3 on 2023-07-31 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="city",
            old_name="created_by",
            new_name="owner",
        ),
    ]