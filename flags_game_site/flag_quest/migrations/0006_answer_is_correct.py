# Generated by Django 4.2.7 on 2023-11-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flag_quest", "0005_remove_answer_correct_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
    ]
