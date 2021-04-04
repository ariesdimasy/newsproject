from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from news.models import Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "created_at",)
