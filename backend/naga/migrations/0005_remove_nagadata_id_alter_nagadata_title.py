# Generated by Django 4.1.7 on 2023-04-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naga", "0004_nagadata_creater"),
    ]

    operations = [
        migrations.RemoveField(model_name="nagadata", name="id",),
        migrations.AlterField(
            model_name="nagadata",
            name="title",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
