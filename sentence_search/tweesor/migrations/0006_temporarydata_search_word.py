# Generated by Django 2.2.10 on 2020-09-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweesor', '0005_temporarydata_temp_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporarydata',
            name='search_word',
            field=models.TextField(default=''),
        ),
    ]
