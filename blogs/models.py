from django.db import models

# Create your models here.
class ArticleCategory(models.Model):
    category_name=models.CharField(max_length=70)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    articlecategory=models.ForeignKey(ArticleCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
