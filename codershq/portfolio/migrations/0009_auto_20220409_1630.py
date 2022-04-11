# Generated by Django 3.2.11 on 2022-04-09 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_rename_experiance_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='job_profile',
        ),
        migrations.AddField(
            model_name='project',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio'),
            preserve_default=False,
        ),
    ]
