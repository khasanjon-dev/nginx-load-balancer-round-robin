from _socket import gethostname

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsModelSerializer, NoneSerializer

count = {gethostname(): 0}


class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer

    @action(['get'], False, 'balance', serializer_class=NoneSerializer)
    def balance(self, request):
        count[gethostname()] += 1
        for i in self.queryset():
            i.save()
        return Response({"message": f"{gethostname()} {count}"})
