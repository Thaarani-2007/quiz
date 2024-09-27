"""
URL configuration for check project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from check import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home , name=""),
    # path('homepage/', views.homepage,name="homepage"),
    # path('welcome/', views.welcome,name= "welcome"),
    path('section/', views.section , name="section"),
    path('Student_Login/', views.Student_Login, name="Student_Login"),
    path('sign-up/', views.signup ,name= "signup"),
    path('quizpage/', views.quizpage ,name= "quizpage"),
    path('quiz/<id>', views.quiz ,name= "quiz"),
    path('about/', views.about ,name= "about"),
    path('logout/', views.logout ,name= "logout"),
]
