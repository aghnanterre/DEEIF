# Generated by Django 2.2 on 2019-04-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(verbose_name='date création')),
                ('date_modification', models.DateTimeField(verbose_name='date modification')),
            ],
        ),
    ]
