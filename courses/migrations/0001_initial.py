# Generated by Django 4.1.7 on 2023-02-20 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('chapterId', models.IntegerField(primary_key=True, serialize=False)),
                ('chapterNumber', models.IntegerField()),
                ('tests', models.CharField(max_length=50)),
                ('materials', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50)),
                ('courseScope', models.DateTimeField()),
                ('courseDescription', models.CharField(max_length=300)),
                ('courseImage', models.ImageField(upload_to='')),
                ('courseBackgroundImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='CourseChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.chapter')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=50)),
                ('chapterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.chapter')),
            ],
        ),
    ]
