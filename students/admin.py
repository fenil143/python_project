from django.contrib import admin
from .models import Student
from .models import StudentCourse
from .models import Payment

# Register your models here

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Id','userName','password','phoneNo','firstName','middleName','lastName','state','city')

admin.site.register(Student,StudentAdmin)

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('userName','courseId')

admin.site.register(StudentCourse,StudentCourseAdmin)    

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('userName','type','amount','expDate')
    
admin.site.register(Payment,PaymentAdmin)
