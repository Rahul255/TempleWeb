from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm1

# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm1
    success_url = reverse_lazy('login')
    template_name = 'signup.html'