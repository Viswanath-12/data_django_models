# Generated by Django 4.2.6 on 2024-01-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessEmployeMentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Series_reference', models.CharField(max_length=200)),
                ('Period', models.FloatField()),
                ('Data_value', models.CharField(max_length=100)),
                ('Suppressed', models.CharField(max_length=100, null=True)),
                ('STATUS', models.CharField(max_length=100)),
                ('UNITS', models.CharField(max_length=100)),
                ('Magnitude', models.IntegerField()),
                ('Subject', models.CharField(max_length=100)),
                ('Group', models.CharField(max_length=100)),
                ('Series_title_1', models.CharField(max_length=100)),
            ],
        ),
    ]
