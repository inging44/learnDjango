from rest_framework import serializers
from sign.models import News
from sign.models import NewsDetail
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'theme_id')

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields = ('id', 'image', 'content')