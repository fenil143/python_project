# Generated by Django 4.1.7 on 2023-04-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_chapter_materials_alter_chapter_tests_and_more'),
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
