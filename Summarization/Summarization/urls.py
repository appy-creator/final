"""Summarization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from Modules.views import (
    home_view,
    about_view,
    contact_view,
    abs_summarize,
    ext_summarize,
    squad_dataset,
    odqa_dataset,
    get_articles,
    get_articles2,
    get_contents,
    get_contents2,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('about/',about_view,name="about"),
    path('contactus/',contact_view,name="contactus"),
    path('dataset/abs_summarize',abs_summarize,name="abs_summarize"),
    path('dataset/ext_summarize',ext_summarize,name="ext_summarize"),
    path('dataset/squad_dataset',squad_dataset,name="squad_dataset"),
    path('dataset/odqa_dataset',odqa_dataset,name="odqa_dataset"),
    path('dataset/<str:dataset>/<str:folder_path>',get_articles,name="get_articles"),
    path('dataset/<str:dataset>/<str:folder_path>',get_articles2,name="get_articles2"),
    path('dataset/<str:dataset>/<str:folder_path>/<str:article>',get_contents,name="get_contents"),
    path('dataset/<str:dataset>/<str:folder_path>/<str:article>',get_contents2,name="get_contents2"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)