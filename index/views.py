import requests
import re

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import template

from index.models import PttArticle, ArticleImage

from bs4 import BeautifulSoup

from index.serializers import PttArticleSerializer, ArticleImageSerializer, ImagesSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PttArticleViewSet(viewsets.ModelViewSet):
    queryset = PttArticle.objects.all()
    serializer_class = PttArticleSerializer
    permission_classes = (IsAuthenticated,)


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated,)


def get_index(request):
    return render(request, 'index.html')


def month_transfer(str):
    switcher = {
        "Jan": "01", "Feb": "02", "Mar": "03",
        "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09",
        "Oct": "10", "Nov": "11", "Dec": "12",
    }
    return switcher.get(str, "00")


def show(request):
    url = request.POST["url"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    post = []
    article_detail = soup.find_all(class_="article-meta-value")
    # 文章標題
    article_title = article_detail[2].text
    # 日期處理
    article_datetime = article_detail[3].text.split(' ')
    year = article_datetime[4]
    month = article_datetime[1]
    day = article_datetime[2]
    time = article_datetime[3]

    # 日期重組格式
    article_datetime = year + "-" + month_transfer(month) + "-" + day + " " + time
    img_urls = soup.find(id='main-content').find_all('a')

    i = PttArticle.objects.create(article_title=article_title, article_date=article_datetime)
    i

    for img_url in img_urls:
        if (img_url['href'].startswith('h') and img_url['href'].find("imgur") != -1):
            ArticleImage.objects.create(image_title=i, image_url=img_url['href'])
            post.append(img_url['href'])
            print(article_title + "," + img_url['href'])

    return render(request, 'show.html', locals())


def gallery(request):
    objs = PttArticle.objects.all()

    for obj in objs:
        print(obj)
        for url in obj.articleimage_set.all():
            print(url.img_url)

    return render(request, 'gallery.html', locals())


def delete(request):
    ArticleImage.objects.all().delete()
    PttArticle.objects.all().delete()
    return HttpResponseRedirect('/index/')
