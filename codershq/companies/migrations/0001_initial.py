# Generated by Django 3.0.11 on 2021-07-30 07:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Comany name')),
                ('logo', models.ImageField(height_field=100, upload_to='logos/', verbose_name='Company logo', width_field=200)),
                ('website', models.URLField(verbose_name='Company website')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorship_type', models.CharField(max_length=100, verbose_name='Company sponsorship type')),
                ('sponsorship_description', models.CharField(max_length=250, verbose_name='Company sponsorship description')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorship_value', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000)], verbose_name='Sponsorship Value')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('sponsorship_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.SponsorshipTypes')),
            ],
        ),
    ]
