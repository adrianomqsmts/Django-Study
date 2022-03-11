from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView

from core.models import PostModel

# Create your views here.
class PostListView(ListView):
    model = PostModel
    template_name = "index.html"
