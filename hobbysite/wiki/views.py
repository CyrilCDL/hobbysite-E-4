from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db import models
from .models import ArticleCategory, Article

# Create your views here.
def article_list(request):
    article = Article.objects.all()
    ctx = {
        'articles': article
    }
    return render(request, 'article_list.html', ctx)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        'article': article
    }
    return render(request, 'article_detail.html', ctx)

class ArticleListView(ListView):
	model = Article
	template_name = "article_list.html"

class ArticleDetailView(DetailView):
	model = Article
	template_name = "article_detail.html"