from rest_framework import serializers
from .models import *
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'