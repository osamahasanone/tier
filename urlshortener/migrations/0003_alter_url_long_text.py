# Generated by Django 3.2.6 on 2021-08-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_alter_url_long_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_text',
            field=models.URLField(max_length=1000),
        ),
    ]
