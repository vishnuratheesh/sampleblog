import random
from tastypie.resources import ModelResource, Resource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import (ApiKeyAuthentication, MultiAuthentication,
                                     SessionAuthentication)
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields, bundle
from tastypie.http import HttpBadRequest, HttpForbidden, HttpApplicationError
from tastypie.exceptions import ImmediateHttpResponse
from articles.models import Article, Category




class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        filtering = {
                     'category':ALL,
                     }
        allowed_methods = ['get','post','patch', 'put']
        authorization = Authorization()
        always_return_data = True 
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())



class ArticleResource(ModelResource):
    category = fields.ForeignKey('articles.api.CategoryResource','category', null=True, full=True)
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'articles'
        filtering = {
                     'category':ALL_WITH_RELATIONS,
                     'published': ['exact', 'lt', 'LtE', 'GtE', 'gt'],
                     'author':ALL_WITH_RELATIONS,
                     'id': ALL,
                     'title': ALL
                     }
        allowed_methods = ['get','post','patch', 'put']
        authorization = Authorization()
        always_return_data = True 
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        detail_uri_name = 'slug'
        
    def dehydrate(self, bundle):
        bundle.data['author_full_name'] = ' '.join([bundle.obj.author.first_name, bundle.obj.author.last_name])
        return bundle 
        
        
        

class ReadNextResource(ModelResource):
    category = fields.ForeignKey('articles.api.CategoryResource','category', null=True, full=True)
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'read_next'
        filtering = {
                     'category':ALL_WITH_RELATIONS,
                     'published': ['exact', 'lt', 'LtE', 'GtE', 'gt'],
                     'author':ALL_WITH_RELATIONS,
                     'id': ALL,
                     'title': ALL
                     }
        allowed_methods = ['get','post','patch', 'put']
        authorization = Authorization()
        always_return_data = True 
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        detail_uri_name = 'slug'
        
    def dehydrate(self, bundle):
        bundle.data['author_full_name'] = ' '.join([bundle.obj.author.first_name, bundle.obj.author.last_name])
        return bundle         
        
    def obj_get_list(self, bundle):
        all_articles  = Article.objects.all()
        read_next = random.sample(all_articles, 4)
        return read_next
    
    
    
        