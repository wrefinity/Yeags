# Generated by Django 4.1.8 on 2023-05-01 14:19

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):
    dependencies = [
        ("world", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="world",
            name="source_path",
            field=models.FilePathField(
                path=pathlib.PurePosixPath(
                    "/Users/boiyelove/Documents/Development/Yeags/yeager_ai/jsonworld"
                )
            ),
        ),
    ]
