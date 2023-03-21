from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('greet/', views.greet, name="hi"),
    path('eat/', views.eat, name="eat well"),
    path('tag/', views.htmlTag, name="html-tag"),
    path('post_detail/<int:pk>/', views.post_detail, name="detail2"),
    path('<int:pk>/',  views.PostDetailView.as_view(), name="detail"),
    path('', views.PostListView.as_view(), name="home2"),
    path('new/', views.PostCreateView.as_view(), name="post_new"),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name="post_delete"),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name="post_edit"),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]