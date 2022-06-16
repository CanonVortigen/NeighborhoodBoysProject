"""meninos_da_vila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url, include
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView
from app.views import CatalogoList, agendamento, CatalogoCreate
from agenda.views import CadastarCliente, DeletarCliente, DetalhesCliente, EditarCliente, HomePage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name="index"),     
    url(r'^contato/$', views.contact, name="contact"),
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'), 
    url(r'^sair/$', LogoutView.as_view(next_page = 'index'), name='logout'),    
    url(r'^conta/', include('accounts.urls', namespace='accounts')),  
    path('catalogo',CatalogoList.as_view(),name='catalogo'),
    path('catalogo/create/', CatalogoCreate.as_view(), name='catalogo-create'),
    path('agendamento', agendamento, name='agendamento'),
    path('home/', HomePage, name='homepage'),
    path('cadastrar-cliente/', CadastarCliente, name='addclient'),
    path('editar-cliente/<int:pk>', EditarCliente, name='updateclient'),
    path('detalhes-cliente/<int:pk>', DetalhesCliente, name='clientdetail'),
    path('deletar-cliente/<int:pk>', DeletarCliente, name='deleteclient'),
    url(r'^admin/', admin.site.urls),    
   

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
