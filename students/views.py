from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Student
from .models import StudentCourse
from courses.models import Course
from courses.models import CourseChapter
from courses.models import Chapter
from courses.models import ChapterVideo
# from .forms import BlogStudent
# Create your views here.

def signin(request):
    return render(request,"signin.html")

def check(request):
    if 'studentName' in request.session:
        s_name = request.session['studentName']
        s_passw = request.session['password']
        s_student = Student.objects.filter(userName=s_name,password=s_passw).values()
        s_stud = s_student[0]
        s_temp = StudentCourse.objects.filter(userName=s_stud['Id']).values()
        s_courses = []
        for crc in s_temp:
            temp1 = Course.objects.filter(courseId=crc['courseId']).values()
            s_courses.append(temp1[0])
        return render(request,"test.html",{'courses': s_courses})
    name = request.POST.get('userName')
    passw = request.POST.get('password')
    student = Student.objects.filter(userName=name, password=passw).values()
    if name == None and passw == None:
        return render(request,"signin.html")
    if student:
        request.session['is_student'] = True
        request.session['studentName'] = name
        request.session['password'] = passw
        stud = student[0]
        print(stud)
        temp = StudentCourse.objects.filter(userName=stud['Id']).values()
        print(temp)
        courses = []
        for crc in temp:
            temp1 = Course.objects.filter(courseId=crc['courseId']).values()
            courses.append(temp1[0])
        return render(request,"test.html",{'courses': courses})
    else:
        error = "please enter valid username and password"
        context = {"error": error}
        return render(request,"signin.html",context)
    
    
def signup(request):
    return render(request,"signup.html")

def signupcheck(request):
    student = Student()
    student.Id = request.POST.get('id')
    student.userName = request.POST.get('userName')
    student.password = request.POST.get('password')
    student.phoneNo = request.POST.get('phoneNo')
    student.firstName = request.POST.get('firstName')
    student.middleName = request.POST.get('middleName')
    # student.lastName = request.POST.get('lastName')
    student.state = request.POST.get('state')
    student.city = request.POST.get('city')
    
    student.save()
    response = redirect("/students/check")
    return response

def search(request):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    courses = Course.objects.all().values()
    if request.GET.get('courseName') != None:
        course = Course.objects.filter(courseName=request.GET.get('courseName')).values()
        return render(request,'search.html',{'course':course[0],'show':course})
    return render(request,"search.html",{'courses': courses})

def chapter(request, id):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    temp = CourseChapter.objects.filter(courseId = id).values()
    chapters = []
    for i in temp:
        temp1 = Chapter.objects.filter(chapterId = i['chapterId_id']).values()
        chapters.append(temp1[0])
        
    return render(request,'chapter.html',{'chapters':chapters})

def explore(request, id):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    chapter = Chapter.objects.filter(chapterId = id).values()
    chapterVideos = ChapterVideo.objects.filter(chapterId = id).values()
    return render(request,'explore.html',{'chapter':chapter[0],'chapterVideos':chapterVideos})

def add(request,name):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    response = redirect('/students/check')
    s_name = request.session['studentName']
    s_passw = request.session['password']
    s_student = Student.objects.filter(userName=s_name,password=s_passw).values()
    s_stud = s_student[0]
    courses = Course.objects.filter(courseName = name).values()
    course = courses[0]
    studentCourses = StudentCourse.objects.filter(userName = s_stud['Id'],courseId = course['courseId']).values()
    print(studentCourses)
    if studentCourses:
        return response
    else:
        student = Student.objects.get(Id = s_stud['Id'])
        temp = StudentCourse()
        temp.userName = student
        temp.courseId = course['courseId']
        print("yes")
        print(temp)
        temp.save()
        return response
    
def about(request):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    return render(request,"about.html")

def services(request):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    return render(request,"services.html")

def feedback(request):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    print(request.GET.get("name"))
    print(request.GET.get("email"))
    print(request.GET.get("phoneNumber"))
    name = request.GET.get("name")
    email = request.GET.get("email")
    phoneNumber = request.GET.get("phoneNumber")
    if name != None and email != None and phoneNumber != None:
        return render(request,"feedback.html",{"message":"Thank you for your feedback"})
    return render(request,"feedback.html",{"message":"None"})

def readMore(request):
    if "studentName" not in request.session:
        response = redirect("/students/signin")
        return response
    if request.session:
        request.session.delete()
    response = redirect("/")
    return response