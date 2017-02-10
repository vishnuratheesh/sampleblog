from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from articles import views
from articles.api import ArticleResource, CategoryResource, ReadNextResource

v1_api = Api(api_name='v1')
v1_api.register(ArticleResource())
v1_api.register(CategoryResource())
v1_api.register(ReadNextResource())


urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name="homepage"),
    url(r'^article-list.html/$', views.ArticleList.as_view(), name="article-list"),
    url(r'^article-detail.html/$', views.ArticleDetail.as_view(), name="article-details"),
    #url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view(), name='article-detail'),
    url(r'^api/', include(v1_api.urls)),
]
