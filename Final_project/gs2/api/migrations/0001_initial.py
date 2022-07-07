# Generated by Django 4.0.5 on 2022-06-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('uploaded_by', models.CharField(max_length=100)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('no_of_downloads', models.IntegerField()),
            ],
        ),
    ]