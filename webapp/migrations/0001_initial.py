# Generated by Django 4.1.7 on 2023-03-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(upload_to='Category')),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
