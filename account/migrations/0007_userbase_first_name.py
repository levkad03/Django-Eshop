# Generated by Django 5.0.1 on 2024-02-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_userbase_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="userbase",
            name="first_name",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
