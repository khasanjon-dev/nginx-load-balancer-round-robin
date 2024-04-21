from rest_framework.serializers import ModelSerializer

from .models import News


class NewsModelSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
