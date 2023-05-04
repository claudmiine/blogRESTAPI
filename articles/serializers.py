# articles/serializers.py
from rest_framework import serializers
from . import models
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'img_name','title', 'category', 'content', 'created_at', 'updated_at',)
        model = models.Article