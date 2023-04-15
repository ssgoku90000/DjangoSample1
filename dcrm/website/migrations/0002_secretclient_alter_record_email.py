# Generated by Django 4.1.7 on 2023-04-15 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="secretClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("options", models.CharField(max_length=50)),
                ("datePosted", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name="record",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]