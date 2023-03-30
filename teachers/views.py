from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Teacher
from .models import TeacherCourse
from courses.models import Course
from courses.models import CourseChapter
from courses.models import Chapter
from courses.models import ChapterVideo
# from .forms import BlogTeacher
# Create your views here.

def signin(request):
    return render(request,"signin.html")

def check(request):
    if 'userName' in request.session:
            s_name = request.session['userName']
            s_passw = request.session['password']
            s_teacher = Teacher.objects.filter(userName=s_name,password=s_passw).values()
            s_stud = s_teacher[0]
            s_temp = TeacherCourse.objects.filter(userName=s_stud['Id']).values()
            s_courses = []
            for crc in s_temp:
                temp1 = Course.objects.filter(courseId=crc['courseId']).values()
                s_courses.append(temp1[0])
            return render(request,"test.html",{'courses': s_courses})
    name = request.POST.get('userName')
    passw = request.POST.get('password')
    teachers = Teacher.objects.filter(userName=name, password=passw).values()
    if name == None and passw == None:
        return render(request,"signin.html")
    if teachers:
        request.session['is_teacher'] = "yes"
        request.session['userName'] = name
        request.session['password'] = passw
        teacher = teachers[0]
        print(teacher)
        temp = TeacherCourse.objects.filter(userName=teacher['Id']).values()
        print(temp)
        courses = []
        for crc in temp:
            temp1 = Course.objects.filter(courseId=crc['courseId']).values()
            courses.append(temp1[0])
        return render(request,'test.html',{'courses': courses})
    else:
        error = "please enter valid username and password"
        context = {"error": error}
        return render(request,"signin.html",context)
    
    
def signup(request):
    return render(request,"signup.html")

def signupcheck(request):
    teachers1 = Teacher.objects.filter(Id = request.POST.get('id')).values()
    if len(teachers1) > 0:
        error = "please select another id"
        return render(request,"signup.html",{"error":error})
    teachers2 = Teacher.objects.filter(userName = request.POST.get('userName')).values()
    if len(teachers2)>0:
        error = "please select another user-name"
        return render(request,"signup.html",{"error":error})
    teacher = Teacher()
    teacher.Id = request.POST.get('id')
    teacher.userName = request.POST.get('userName')
    teacher.password = request.POST.get('password')
    teacher.phoneNo = request.POST.get('phoneNo')
    teacher.firstName = request.POST.get('firstName')
    teacher.middleName = request.POST.get('middleName')
    # teacher.lastName = request.POST.get('lastName')
    teacher.state = request.POST.get('state')
    teacher.city = request.POST.get('city')
    
    teacher.save()
    response = redirect("/teachers/check")
    return response

def about(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"about.html")

def services(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"services.html")

def feedback(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    name = request.GET.get("name")
    email = request.GET.get("email")
    phoneNumber = request.GET.get("phoneNumber")
    if name != None and email != None and phoneNumber != None:
        return render(request,"feedback.html",{"message":"Thank you for your feedback"})
    return render(request,"feedback.html",{"message":"None"})
    
def create(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"create.html")

def save(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    c_id = request.GET.get("courseId")
    c_name = request.GET.get("courseName")
    c_scope = request.GET.get("courseScope")
    c_description = request.GET.get("courseDescription")
    c_image = request.GET.get("backgroundImage")
    userName = request.GET.get("userName")
    password = request.GET.get("password")
    course = Course.objects.filter(courseId = c_id).values()
    teachers = Teacher.objects.filter(userName = userName,password = password).values()
    if course:
        error = "Please select another course-id"
        return render(request,"create.html",{"error":error})
    if len(teachers) == 0:
        error = "please enter valid username and password"
        return render(request,"create.html",{"error":error})
    else:
        temp = Course()
        temp.courseId = c_id
        temp.courseName = c_name
        temp.courseDescription = c_description
        temp.courseImage = c_image
        temp.courseScope = c_scope
        temp.save()
        foo = teachers[0]
        teacher = Teacher.objects.get(Id = foo['Id'])
        temp1 = TeacherCourse()
        temp1.userName = teacher
        temp1.courseId = c_id
        temp1.save()
        response = redirect("/teachers/check")
        return response
    
def chapter(request, id):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    request.session["courseId"] = id
    temp = CourseChapter.objects.filter(courseId = id).values()
    chapters = []
    for i in temp:
        temp1 = Chapter.objects.filter(chapterId = i['chapterId_id']).values()
        chapters.append(temp1[0])
        
    return render(request,'chapter.html',{'chapters':chapters})

def createChapter(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"createChapter.html")
        
def saveChapter(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    c_id = request.GET.get('chapterId')
    c_number = request.GET.get('chapterNumber')
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    testLink = request.GET.get('testLink')
    materialLink = request.GET.get('materialLink')
    chapter = Chapter.objects.filter(chapterId = c_id).values()
    check = True if userName == request.session['userName'] and password == request.session['password'] else False
    if chapter:
        error = "Please select another course-id"
        return render(request,"createChapter.html",{"error":error})
    if check == False:
        error = "please enter valid username and password"
        return render(request,"createChapter.html",{"error":error})
    else:
        temp = Chapter()
        temp.chapterId = c_id
        temp.chapterNumber = c_number
        temp.tests = testLink
        temp.materials = materialLink
        temp.save()
        temp_course = Course.objects.get(courseId = request.session["courseId"])
        temp_chapter = Chapter.objects.get(chapterId = c_id)
        temp1 = CourseChapter()
        temp1.courseId = temp_course
        temp1.chapterId = temp_chapter
        temp1.save()
        num = (request.session['courseId'])
        str1 = "/teachers/chapter/"+str(num)
        print(str)
        response = redirect(str1)
        return response
    
def explore(request, id):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    request.session["chapterId"] = id
    chapter = Chapter.objects.filter(chapterId = id).values()
    chapterVideos = ChapterVideo.objects.filter(chapterId = id).values()
    return render(request,'explore.html',{'chapter':chapter[0],'chapterVideos':chapterVideos})

def updateChapter(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"updateChapter.html")

def update(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    testLink = request.GET.get('testLink')
    materialLink = request.GET.get('materialLink')
    c_id = request.session["chapterId"]
    check = True if userName == request.session['userName'] and password == request.session['password'] else False
    if check == False:
        error = "please enter valid username and password"
        return render(request,"updateChapter.html",{"error":error})
    else:
        temp = Chapter.objects.get(chapterId = c_id)
        if testLink:
            print("hello1")
            temp.tests = testLink
        if materialLink:
            print("hello2")
            temp.materials = materialLink
        temp.save()
        return render(request,"updateChapter.html")
    
def deleteChapter(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    return render(request,"deleteChapter.html")

def delete(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    Id1 = request.GET.get('chapterId')
    chapter = Chapter.objects.get(chapterId = Id1)
    chapter.delete()
    num = (request.session['courseId'])
    str1 = "/teachers/chapter/"+str(num)
    response = redirect(str1)
    return response

def readMore(request):
    if "userName" not in request.session:
        response = redirect("/teachers/signin")
        return response
    if request.session:
        request.session.delete()
    response = redirect("/")
    return response