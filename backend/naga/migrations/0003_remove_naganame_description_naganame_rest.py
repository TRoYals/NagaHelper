# Generated by Django 4.1.7 on 2023-04-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naga", "0002_rename_nagadate_nagadata"),
    ]

    operations = [
        migrations.RemoveField(model_name="naganame", name="description",),
        migrations.AddField(
            model_name="naganame", name="rest", field=models.IntegerField(default=0),
        ),
    ]