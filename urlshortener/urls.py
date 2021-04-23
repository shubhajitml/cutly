"""urlshortener URL Configuration

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
from django.urls import path
from authenticator.views import signup_view, login_view, logout_view
from shortener.views import home_view, dashboard_view, generate_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

    path('', home_view, name="home"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('generate/', generate_view, name="generate"),
    path('delete/', delete_view, name="delete"),
    path('<str:query>/', home_view, name="home"),
]
