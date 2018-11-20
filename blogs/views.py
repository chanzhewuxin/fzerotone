from django.shortcuts import render

from blogs.models import Article, ArticleCategory
# Create your views here.


def index(request):
    # 获取所有文章
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'blogs/index.html', context)
