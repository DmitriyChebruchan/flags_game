# Generated by Django 4.2.7 on 2023-12-05 18:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flag_quest", "0002_countryinfo_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="countryinfo",
            name="test",
        ),
    ]
