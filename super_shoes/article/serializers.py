from models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'description', "price", "total_in_shelf", "total_in_vault", "id", "store", "store_name")
