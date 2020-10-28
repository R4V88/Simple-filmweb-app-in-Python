# Generated by Django 3.1.2 on 2020-10-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0006_auto_20201025_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Dramat'), (2, 'Komedia'), (0, 'Inne'), (1, 'Horror'), (3, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='filmyweb.Film')),
            ],
        ),
    ]
