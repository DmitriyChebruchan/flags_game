# Generated by Django 4.2.7 on 2023-11-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flag_quest", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="countryinfo",
            name="capital",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
