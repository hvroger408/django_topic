# Generated by Django 2.2.12 on 2020-12-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]