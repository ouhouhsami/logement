# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-08 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0017_auto_20170308_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actortag',
            options={'verbose_name': 'Mots-cl\xe9 Acteur'},
        ),
        migrations.AlterModelOptions(
            name='actortagorder',
            options={'verbose_name': 'Relation Acteur - Mots-cl\xe9'},
        ),
        migrations.AlterModelOptions(
            name='experiencetag',
            options={'verbose_name': 'Mots-cl\xe9 Exp\xe9rience'},
        ),
        migrations.AlterModelOptions(
            name='experiencetagorder',
            options={'verbose_name': 'Relation Experience - Mots-cl\xe9'},
        ),
        migrations.AlterField(
            model_name='experience',
            name='tags',
            field=models.ManyToManyField(through='appli.ExperienceTagOrder', to='appli.ExperienceTag'),
        ),
        migrations.AlterField(
            model_name='experiencetagorder',
            name='order',
            field=models.PositiveIntegerField(blank=True, verbose_name='n\xb0 ordre'),
        ),
    ]