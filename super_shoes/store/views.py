from models import Store
from rest_framework import viewsets
from .serializers import StoreSerializer
from rest_framework.response import Response


class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Store.objects.all().order_by('-pk')
    serializer_class = StoreSerializer

    def retrieve(self, request, *args, **kwargs):
        r = super(StoreViewSet, self).retrieve(request, args, kwargs)
        print "retrieve", r, args, kwargs
        return r

    def list(self, request, *args, **kwargs):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        elements = len(serializer.data)
        return Response({"total_elements": elements,
                         "success": True,
                         "stores": serializer.data})

