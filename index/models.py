from django.db import models


class PttArticle(models.Model):
    article_title = models.CharField(max_length=100)
    article_date = models.CharField(max_length=100)

    def __str__(self):
        return self.article_title


class ArticleImage(models.Model):
    image_title = models.ForeignKey('PttArticle', related_name='article_images', on_delete=models.CASCADE, default='')
    image_url = models.URLField(max_length=100)

    def __str__(self):
        return self.image_title.article_title
