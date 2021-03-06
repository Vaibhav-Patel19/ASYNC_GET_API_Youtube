# Generated by Django 4.0 on 2021-12-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('video_description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]
