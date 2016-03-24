from models import Store
from rest_framework import viewsets
from .serializers import StoreSerializer
from rest_framework.response import Response
from rest_framework import exceptions

from store.forms import StoreModelForm
from django.shortcuts import render
from django.template import RequestContext


def new_store_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StoreModelForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, "success.html")
    else:
        form = StoreModelForm()
    return render(request, "new_store.html", {"form": form},
                  context_instance=RequestContext(request))


class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Store.objects.all().order_by('-pk')
    serializer_class = StoreSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        queryset = Store.objects.get(pk=pk)
        serializer = StoreSerializer(queryset)
        return Response({"store": serializer.data, "success": True})

    def list(self, request, *args, **kwargs):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        elements = len(serializer.data)
        return Response({"total_elements": elements,
                         "success": True,
                         "stores": serializer.data})

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        print "lalalalalala"
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.PermissionDenied,
                            exceptions.AuthenticationFailed)):
            response = Response({"success": False, "error_code": 401,
                                 "error_msg": "Not authorized"})
        else:
            response = Response({"success": False, "error_code": 500,
                                 "error_msg": "Server Error"})

        response.exception = True
        return response
