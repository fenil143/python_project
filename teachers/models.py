from django.db import models

# Create your models here.

class Teacher(models.Model):
    Id = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length = 50)
    phoneNo = models.IntegerField()
    firstName = models.CharField(max_length = 50)
    middleName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    state = models.CharField(max_length= 50)
    city = models.CharField(max_length = 50)
    
class AccountDetail(models.Model):
    userName = models.ForeignKey("Teacher",on_delete=models.CASCADE)
    accountNumber = models.IntegerField()
    amountNumber = models.IntegerField()
    
class TeacherCourse(models.Model):
    userName = models.ForeignKey("Teacher",on_delete=models.CASCADE)
    courseId = models.IntegerField()
    

