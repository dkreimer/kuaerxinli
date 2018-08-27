from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
