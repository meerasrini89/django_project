# Generated by Django 3.2 on 2022-09-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="corn",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="corn",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
