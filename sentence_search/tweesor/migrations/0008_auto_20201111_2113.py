# Generated by Django 2.2.10 on 2020-11-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweesor', '0007_auto_20201010_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='learntweet',
            name='iine_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learntweet',
            name='retweet_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temporarydata',
            name='temp_iine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temporarydata',
            name='temp_retweet',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]