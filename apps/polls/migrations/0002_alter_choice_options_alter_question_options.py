# Generated by Django 4.0.10 on 2023-02-19 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="choice",
            options={"verbose_name": "Choice", "verbose_name_plural": "Choices"},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"verbose_name": "Question", "verbose_name_plural": "Questions"},
        ),
    ]
