# Generated by Django 3.2 on 2021-04-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0003_auto_20210418_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleattributes',
            name='Thumbnail',
            field=models.CharField(max_length=200),
        ),
    ]