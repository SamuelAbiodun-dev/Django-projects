from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('resetpassword/', views.ResetPasswordView.as_view(), name="reset_password"),
    ]
