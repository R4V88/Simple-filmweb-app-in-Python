# Generated by Django 3.1.2 on 2020-10-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0003_auto_20201025_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Sci-fi'), (4, 'Dramat'), (2, 'Komedia'), (1, 'Horror'), (0, 'Inne')], default=0),
        ),
    ]
