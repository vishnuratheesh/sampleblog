import random
from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView, DetailView
from django.utils import timezone as tz
from django.views.generic.base import View, TemplateView


def get_read_next():
    all_articles  = Article.objects.all()
    read_next = random.sample(all_articles, 4)
    return read_next


class Homepage(TemplateView):
    template_name = 'base.html'
   

class ArticleList(TemplateView):
    template_name = 'article_list.html'

   
class ArticleDetail(TemplateView):
    template_name = 'article_detail.html'
   

'''
# Create your views here.
class ArticleList(ListView):
    model  = Article
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        all_articles  = Article.objects.filter(published__lt = tz.now())
        print all_articles
        main_article = random.sample(all_articles, 1)[0]
        context['main_article'] = main_article
        context['read_next'] = get_read_next()
        return context

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['read_next'] = get_read_next()
        return context
    
'''