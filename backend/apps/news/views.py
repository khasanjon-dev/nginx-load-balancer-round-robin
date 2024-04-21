from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsModelSerializer


class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
