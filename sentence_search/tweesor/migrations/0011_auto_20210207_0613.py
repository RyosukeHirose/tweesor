# Generated by Django 2.2.10 on 2021-02-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweesor', '0010_learntweet_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learntweet',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
