from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def test(request):
    a = 4
    data = {
        'value': a
    }
    return render(request,'test.html',data)


def welcome(request):
    if request.method == 'POST':
        message ="We will contact you within 24 hours"
        return render(request,"welcome.html",{'message':message})
    return render(request,'welcome.html')

def logout(request):
    if request.session:
        request.session.delete()
    response = redirect("/")
    return response