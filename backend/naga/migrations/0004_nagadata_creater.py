# Generated by Django 4.1.7 on 2023-04-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naga", "0003_remove_naganame_description_naganame_rest"),
    ]

    operations = [
        migrations.AddField(
            model_name="nagadata",
            name="creater",
            field=models.CharField(default="null", max_length=20),
        ),
    ]
