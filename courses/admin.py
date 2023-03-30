from django.contrib import admin
from .models import Course
from .models import CourseChapter
from .models import Chapter
from .models import ChapterVideo
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseId','courseName','courseScope','courseDescription','courseImage','courseBackgroundImage')
    
admin.site.register(Course,CourseAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapterId','chapterNumber','tests','materials')
    
admin.site.register(Chapter,ChapterAdmin)

class ChapterVideoAdmin(admin.ModelAdmin):
    list_display = ('chapterId','video')
    
admin.site.register(ChapterVideo,ChapterVideoAdmin)

class CourseChapterAdmin(admin.ModelAdmin):
    list_display = ('courseId','chapterId')
    
admin.site.register(CourseChapter,CourseChapterAdmin)