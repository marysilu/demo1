# Generated by Django 4.1.3 on 2022-11-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=150)),
                ('timg', models.ImageField(upload_to='pics')),
                ('desig', models.CharField(max_length=200)),
                ('tabot', models.TextField()),
            ],
        ),
    ]
