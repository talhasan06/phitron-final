from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect


# Create your views here.
class UserRegistrationFormView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(View):
     def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))
