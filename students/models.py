from django.db import models


class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    userName = models.CharField( max_length=50)
    password = models.CharField(max_length = 50)
    phoneNo = models.IntegerField()
    firstName = models.CharField(max_length = 50)
    middleName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    state = models.CharField(max_length= 50)
    city = models.CharField(max_length = 50)
    
class Payment(models.Model):
    userName = models.ForeignKey("Student",on_delete=models.CASCADE)
    type = models.CharField(max_length = 50)
    amount = models.IntegerField()
    expDate = models.DateTimeField()
    
class StudentCourse(models.Model):
    userName = models.ForeignKey("Student",on_delete=models.CASCADE)
    courseId = models.IntegerField()