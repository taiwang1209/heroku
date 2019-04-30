from rest_framework import serializers

from index.models import PttArticle, ArticleImage


class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        # fields = '__all__'
        fields = ('image_title', 'image_url')


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        fields = ('image_title', 'image_url')
        # fields = ('id', 'image_url')


class PttArticleSerializer(serializers.ModelSerializer):
    article_images = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = PttArticle
        fields = ('id', 'article_title', 'article_date', 'article_images')
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
