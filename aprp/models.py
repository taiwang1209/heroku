from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='categoty', on_delete=models.CASCADE, default='')
    market = models.ForeignKey('Market', related_name='market', on_delete=models.CASCADE, default='')


class DailyTran(models.Model):
    name = models.ForeignKey('Product', related_name='dailytrans', on_delete=models.CASCADE, default='')
    up_price = models.CharField(max_length=100)
    low_price = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name.name
