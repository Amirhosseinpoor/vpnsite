from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


# Create your views here.
from django.shortcuts import render

# Create your views here.
