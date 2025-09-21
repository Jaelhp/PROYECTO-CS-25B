from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect   # 👈 importa redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('admin/dashboard/', lambda r: HttpResponse('Admin dashboard (placeholder)')),
    
    # 👇 nueva línea: redirigir la raíz al login
    path('', lambda request: redirect('accounts:login')),
]
