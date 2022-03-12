from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'create.html'
    success_url = reverse_lazy('login')

class LogoutView(View):
    # Responde apenas requisições GET
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
    
class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        username = form["username"].data
        password = form["password"].data
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginFormView, self).form_valid(form)
        else:
            return self.form_invalid(form)
     
class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'update.html'
    success_url = reverse_lazy('index')
    fields = ['username', 'first_name', 'last_name']
    
    def get_object(self):
        return self.request.user
    

class UserPasswordUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'password.html'
    success_url = reverse_lazy('index')
    
    def get_form_class(self):
        return PasswordChangeForm
        
    def get_object(self):
        return self.request.user
    
    def get(self, request, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})
        
class UserDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
    
    