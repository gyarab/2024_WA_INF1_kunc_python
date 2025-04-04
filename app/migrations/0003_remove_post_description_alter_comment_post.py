# Generated by Django 5.1.6 on 2025-02-11 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_tag_posts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="description",
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="app.post",
            ),
        ),
    ]
