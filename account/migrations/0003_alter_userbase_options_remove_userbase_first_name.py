# Generated by Django 5.0.1 on 2024-02-06 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_userbase_options_userbase_first_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userbase",
            options={"verbose_name": "Account", "verbose_name_plural": "Accounts"},
        ),
        migrations.RemoveField(
            model_name="userbase",
            name="first_name",
        ),
    ]
