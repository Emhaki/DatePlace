# Generated by Django 5.1.2 on 2024-10-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateplace',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dateplace',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dateplace',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
