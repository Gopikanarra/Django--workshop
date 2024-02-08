"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from VVITApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('g/<str:n>/',views.greet),
    path('welcome/',views.ky),
    path('p/<str:en>/<int:es>/',views.emp),
    path('home/<str:a>/<str:b>/',views.home),	
    path('t/<str:name>/<str:roll>/<str:branch>/<int:year>',views.tables),
    # path('temps/<str:name>/<str:role>/',views.func),
    path('emps/<str:name>/<int:salary>/<str:company>/<str:designation>/',views.employee),
    path('forms/',views.forms),
    path('',include('BSApp.urls')),
]




