from django.contrib import admin
from .models import Teacher
from .models import TeacherCourse

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('Id','userName','password','phoneNo','firstName','middleName','lastName','state','city')
    
admin.site.register(Teacher,TeacherAdmin)

class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ('userName','courseId')
    
admin.site.register(TeacherCourse,TeacherCourseAdmin)
    

