from rest_framework import viewsets
from .models import *
from .serializers import ArticleSerializer
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = food.objects.all()
    serializer_class = ArticleSerializer