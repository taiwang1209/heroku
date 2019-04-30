from django.contrib import admin

from aprp.models import Category, Market, Product, DailyTran


admin.site.register(Category)
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(DailyTran)
