from models import Article
from store.models import Store
from rest_framework import viewsets
from .serializers import ArticleSerializer
from rest_framework.response import Response


class ArticlebyStoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    http_method_names = ['get', ]

    def list(self, request, *args, **kwargs):
        print kwargs
        store_pk = kwargs["store_pk"]
        if not store_pk.isdigit():
            return Response({"success": False, "error_msg": "Bad Request",
                             "error_code": 400})
        try:
            store = Store.objects.get(pk=store_pk)
        except Store.DoesNotExist:
            return Response({"success": False, "error_msg": "Record not Found",
                             "error_code": 404})
        queryset = Article.objects.filter(store=store)
        serializer = ArticleSerializer(queryset, many=True,
                                       context={'request': request})
        elements = len(serializer.data)
        return Response({"total_elements": elements,
                         "success": True,
                         "articles": serializer.data})


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Article.objects.get(pk=kwargs["pk"])
        serializer = ArticleSerializer(queryset, context={'request': request})
        return Response({"article": serializer.data, "success": True})

    def list(self, request, *args, **kwargs):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True,
                                       context={'request': request})
        elements = len(serializer.data)
        return Response({"total_elements": elements,
                         "success": True,
                         "articles": serializer.data})
