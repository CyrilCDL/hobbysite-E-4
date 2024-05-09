from django.urls import path
from .views import CategoryListView, ArticleDetailView

urlpatterns = [
    path('blog/articles',CategoryListView.as_view(), name="articlelist"),
    path('blog/article/<int:pk>',ArticleDetailView.as_view(), name='category'),

]

app_name ="blog"