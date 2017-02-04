from django.conf.urls import include, url
from django.contrib import admin
from articles import views


urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name="homepage"),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view(), name='article-detail'),
]
