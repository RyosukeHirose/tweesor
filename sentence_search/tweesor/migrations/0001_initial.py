# Generated by Django 2.2.10 on 2020-06-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearnTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField()),
                ('text', models.TextField()),
                ('text_list', models.TextField()),
                ('tag', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_tweet_id', models.IntegerField()),
                ('temp_text', models.TextField()),
            ],
        ),
    ]
