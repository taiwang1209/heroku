from rest_framework import serializers

from aprp.models import Category, Market, Product, DailyTran


class DailyTranSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DailyTran
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    dailytrans = DailyTranSerializer(many=True, read_only=True)
    category = serializers.SerializerMethodField(source='get_category')
    market = serializers.SerializerMethodField(source='get_market')

    class Meta:
        model = Product
        fields = ('name', 'category', 'market', 'dailytrans')

    def get_category(self, obj):
        return obj.category.name

    def get_market(self, obj):
        return obj.market.name


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name')

