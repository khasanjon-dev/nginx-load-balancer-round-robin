from socket import gethostname

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsModelSerializer, NoneSerializer

count = 0

class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer

    @action(detail=False, methods=['get'], url_path='counter', serializer_class=NoneSerializer)
    def counter(self, request):
        global count
        count += 1
        return Response({
            gethostname(): count
        })