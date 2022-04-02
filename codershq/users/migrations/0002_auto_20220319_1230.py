# Generated by Django 3.2.11 on 2022-03-19 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamtrophyrecord',
            name='team',
        ),
        migrations.RemoveField(
            model_name='userscore',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userscore',
            name='user_score_category',
        ),
        migrations.RemoveField(
            model_name='usertrophyrecord',
            name='trophy_type',
        ),
        migrations.RemoveField(
            model_name='usertrophyrecord',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='academic_qualification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='github_profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='teams',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamTrophyRecord',
        ),
        migrations.DeleteModel(
            name='UserScore',
        ),
        migrations.DeleteModel(
            name='UserScoreCategory',
        ),
        migrations.DeleteModel(
            name='UserTrophyRecord',
        ),
        migrations.DeleteModel(
            name='UserTrophyType',
        ),
    ]
