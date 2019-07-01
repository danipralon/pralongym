"""pralongym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from . import settings

urlpatterns = [
    #carrega a página de administrador
    path('admin/', admin.site.urls),

    #carrega o login
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    
    #desconecta o usuário
    path('logout/',views.logout_user),

    #leva a página principal    
    path('', views.index),

    #
    path('planos/',views.planos),

    path('dados/all/',views.dados_all),

    path('dados/detail/<id>/',views.dados_detail),
    
    path('dados/register/',views.register_dados),
    
    path('dados/register/submit', views.set_cliente)
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
