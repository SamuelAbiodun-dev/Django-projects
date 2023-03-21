from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class ResetPasswordView(generic.UpdateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')
    template_name = 'account/password_reset_form.html'


