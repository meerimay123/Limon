# Generated by Django 5.0.7 on 2024-07-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('created_date', models.DateField()),
            ],
        ),
    ]