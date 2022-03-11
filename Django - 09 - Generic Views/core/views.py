from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView

from core.models import PostModel

# Create your views here.
class PostListView(ListView):
    model = PostModel
    template_name = "index.html"

class PostDetailView(DetailView):
    model = PostModel
    context_object_name = 'post'
    template_name = "details.html"
    
class PostDeleteView(DeleteView):
    model = PostModel
    template_name = "delete.html"
    success_url = reverse_lazy('index')

class PostCreateView(CreateView):
    model = PostModel
    template_name = "create.html"
    fields = '__all__'
    success_url = reverse_lazy('index')
