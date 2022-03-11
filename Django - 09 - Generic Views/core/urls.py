from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>", PostDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="delete"),
    path("create", PostCreateView.as_view(), name="create")
]
