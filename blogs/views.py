from django.shortcuts import render

from blogs.models import Article, ArticleCategory, ArticleTag
# Create your views here.


def index(request):
    # 获取所有文章
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()
    tags = ArticleTag.objects.all()
    context = {'articles': articles, 'categories': categories, 'tags': tags}
    return render(request, 'blogs/index.html', context)
