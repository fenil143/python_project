from django.db import models


class Course(models.Model):
    courseId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseScope = models.DateTimeField()
    courseDescription = models.CharField(max_length=300)
    courseImage = models.ImageField()
    courseBackgroundImage = models.ImageField()

class Chapter(models.Model):
    chapterId = models.IntegerField(primary_key=True)
    chapterNumber = models.IntegerField()
    tests = models.CharField(max_length=500)
    materials = models.CharField(max_length=500)

class ChapterVideo(models.Model):
    chapterId = models.ForeignKey('Chapter',on_delete=models.CASCADE)
    video = models.CharField(max_length=500)
    
class CourseChapter(models.Model):
    courseId = models.ForeignKey('Course',on_delete=models.CASCADE)
    chapterId = models.ForeignKey('Chapter',on_delete=models.CASCADE)
    
