from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('/signin',views.signin),
    path('/check',views.check),
    path('/signup',views.signup),
    path("/check-signup",views.signupcheck),
    path("/about",views.about),
    path("/services",views.services),
    path("/feedback",views.feedback),
    path("/create",views.create),
    path("/save",views.save),
    path("/saveChapter",views.saveChapter),
    path("/chapter/<int:id>",views.chapter),
    path("/create-chapter",views.createChapter),
    path("/deleteChapter",views.deleteChapter),
    path("/delete",views.delete),
    path("/explore/<int:id>",views.explore),
    path("/updateChapter",views.updateChapter),
    path("/readMore",views.readMore),
    path("/update",views.update),
]