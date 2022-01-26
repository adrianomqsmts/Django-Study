from django.urls import path
from django.views.generic.base import View
from .views import index, success

urlpatterns = [
    path('', index.as_view(), name = 'index'),
    path('success', success.as_view(), name = 'success'),
]
