# Generated by Django 5.1.6 on 2025-02-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author_name",
            field=models.CharField(default="Anonymous", max_length=100),
        ),
    ]
