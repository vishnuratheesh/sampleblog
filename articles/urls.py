from django.conf.urls import include, url
from django.contrib import admin
from articles import views

urlpatterns = [
    url(r'^$', views.ArticleList.as_view()),
]
