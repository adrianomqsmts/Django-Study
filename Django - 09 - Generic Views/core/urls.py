from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>", PostDetailView.as_view(), name="detail")
]
