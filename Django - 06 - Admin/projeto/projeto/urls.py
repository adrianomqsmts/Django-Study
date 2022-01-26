from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

admin.AdminSite.site_header = 'Área de ADM'
admin.AdminSite.site_title = 'Bem-vindo'
admin.AdminSite.index_title = 'ADM'