# Generated by Django 3.2.17 on 2023-02-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('college_name', models.CharField(max_length=255)),
            ],
        ),
    ]
