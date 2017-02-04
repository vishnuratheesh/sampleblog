import random
from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView, DetailView


def get_read_next():
    all_articles  = Article.objects.all()
    read_next = random.sample(all_articles, 4)
    return read_next


# Create your views here.
class ArticleList(ListView):
    model  = Article
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['main_article'] = Article.objects.get(pk=1)
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