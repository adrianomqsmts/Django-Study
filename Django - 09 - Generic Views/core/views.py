from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from core.models import PostModel

# Create your views here.
class PostListView(ListView):
    model = PostModel
    template_name = "index.html"

class ModelDetailView(DetailView):
    model = PostModel
    context_object_name = 'post'
    template_name = "details.html"
