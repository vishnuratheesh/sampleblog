from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView, DetailView

# Create your views here.
class ArticleList(ListView):
    model  = Article
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['main_article'] = Article.objects.get(pk=1)
        return context