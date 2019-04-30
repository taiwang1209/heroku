import json

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from aprp.serializers import CategorySerializer, MarketSerializer, ProductSerializer, DailyTranSerializer
from aprp.models import Category, Market, Product, DailyTran


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class MarketList(ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = (IsAuthenticated,)


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class DailyTranList(ListCreateAPIView):
    queryset = DailyTran.objects.all()
    serializer_class = DailyTranSerializer
    permission_classes = (IsAuthenticated,)
