# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=10)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'tip', max_length=10, choices=[(b'tip', b'TIP'), (b'url', b'LINK'), (b'longform', b'LONGFORM')])),
                ('title', models.TextField(max_length=140)),
                ('content', models.TextField(max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('location', models.ForeignKey(to='main.Location', null=True)),
                ('originalPoster', models.ForeignKey(to='main.Poster', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(related_name='related_story', to='main.Tag'),
        ),
    ]
