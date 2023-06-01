# Generated by Django 4.2.1 on 2023-06-01 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
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
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(blank=True, upload_to="listings/")),
                ("category", models.CharField(blank=True, max_length=64)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("college", models.CharField(blank=True, max_length=64)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Active", "Active"),
                            ("Sold", "Sold"),
                            ("Expired", "Expired"),
                        ],
                        default="Active",
                        max_length=64,
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("New", "New"),
                            ("Almost New", "Almost New"),
                            ("Used", "Used"),
                            ("Very Used", "Very Used"),
                            ("Okayish", "Okayish"),
                        ],
                        default="New",
                        max_length=64,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="listings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
