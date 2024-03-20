from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


def article_list(request):
    article = Article.objects.all()
    ctx = {'articles': article,  
           }
    return render(request, 'article_list.html', ctx)

def article_detail(request, id):
    article = Article.objects.get(id=id)
    ctx = {'article': article,  
           }
    return render(request, 'article_detail.html', ctx)

class CategoryListView(ListView):
    model = Article
    template_name = "blog_list.html"

class ArticleDetailView (DetailView):
    model = Article
    template_name = "blog_detail.html"

