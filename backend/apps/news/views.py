from rest_framework.viewsets import ModelViewSet

from .serializers import NewsModelSerializer
from ..news.models import News


class NewsModelViewSet(ModelViewSet):
    queryset = News
    serializer_class = NewsModelSerializer
