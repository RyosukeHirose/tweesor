# Generated by Django 2.2.10 on 2020-12-12 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweesor', '0008_auto_20201111_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='learntweet',
            name='follow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learntweet',
            name='followers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learntweet',
            name='user_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='temporarydata',
            name='temp_follow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temporarydata',
            name='temp_followers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temporarydata',
            name='temp_user_name',
            field=models.TextField(default=''),
        ),
    ]
