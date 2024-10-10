# Generated by Django 5.1.1 on 2024-10-05 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_comment_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to='tasks.task'),
        ),
    ]
