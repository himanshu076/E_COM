# Generated by Django 4.2.2 on 2023-06-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cotegories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="store_name",
            field=models.CharField(max_length=115, unique=True),
        ),
    ]
