from django.conf.urls import patterns, url, include
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the
# browsable API.
urlpatterns = patterns("",
                       url(r'^', include(router.urls))
                       )
