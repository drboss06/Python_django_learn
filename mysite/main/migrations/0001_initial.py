# Generated by Django 4.0.2 on 2022-02-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_memorie', models.CharField(max_length=150, verbose_name='Name')),
                ('date_memorie', models.DateField(verbose_name='Date of memorie')),
                ('description_memorie', models.TextField()),
            ],
        ),
    ]
