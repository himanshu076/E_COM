# Generated by Django 4.2.2 on 2023-06-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={"verbose_name_plural": "Product Images"},
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(upload_to="media/product/"),
        ),
    ]
