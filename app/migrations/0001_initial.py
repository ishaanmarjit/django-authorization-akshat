# Generated by Django 3.2.5 on 2021-09-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('author', models.CharField(max_length=25)),
                ('cover', models.ImageField(upload_to='book_covers')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]