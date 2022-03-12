from unicodedata import name
from django.urls import path, include
from .views import IndexView, LogoutView, UserCreateView, LoginFormView, UserUpdateView, UserPasswordUpdateView, UserDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("users/create", UserCreateView.as_view(), name='create'),
    path("users/logout", LogoutView.as_view(), name='logout'),
    path("users/login", LoginFormView.as_view(), name='login'),
    path("users/update", UserUpdateView.as_view(), name='update'),
    path("users/password", UserPasswordUpdateView.as_view(), name='password'),
    path("users/delete", UserDeleteView.as_view(), name='delete'),
]
