# Generated by Django 4.1.7 on 2023-05-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_userdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(blank=True, max_length=100, null=True)),
                ('proquantity', models.IntegerField(blank=True, null=True)),
                ('proprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
