# Generated by Django 4.2 on 2023-04-25 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="is_complete",
            new_name="is_completed",
        ),
        migrations.AlterField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="projects.project",
            ),
        ),
    ]
