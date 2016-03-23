from django.conf.urls import patterns, url, include
from rest_framework import routers
from article.views import ArticleViewSet, ArticlebyStoreViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'articles/stores/(?P<store_pk>[^/.]+)', ArticlebyStoreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the
# browsable API.
urlpatterns = patterns("",
                       url(r'^', include(router.urls))
                       )
