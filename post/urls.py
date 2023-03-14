from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('greet', views.greet, name="hi"),
    path('eat', views.eat, name="eat well"),
    path('tag', views.htmlTag, name="html-tag"),
]
