from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('signin',views.signin),
    path('check',views.check),
    path('signup',views.signup),
    path("check-signup",views.signupcheck),
    path("search",views.search),
    path("chapter/<int:id>",views.chapter),
    path("explore/<int:id>",views.explore),
    path("add/<name>",views.add),
    path("about",views.about),
    path("services",views.services),
    path("feedback",views.feedback),
    path("readMore",views.readMore),
    # path('teachers/',include('teachers.urls')),
    # path('courses/',include('courses.urls')),
]