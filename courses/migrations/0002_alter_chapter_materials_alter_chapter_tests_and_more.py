# Generated by Django 4.1.7 on 2023-03-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='materials',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='tests',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='chaptervideo',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
