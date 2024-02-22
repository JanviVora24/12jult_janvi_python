# Generated by Django 4.2.7 on 2023-12-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=180)),
                ('cate', models.CharField(max_length=180)),
                ('myfile', models.FileField(upload_to='Media')),
                ('comment', models.TextField()),
            ],
        ),
    ]
