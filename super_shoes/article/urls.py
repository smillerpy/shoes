from django.conf.urls import url, include
from rest_framework import routers
from article.views import ArticleViewSet, ArticlebyStoreViewSet
from article import views

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'articles/stores/(?P<store_pk>[^/.]+)', ArticlebyStoreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the
# browsable API.
urlpatterns = [
    url("^new_article$", views.new_article_view, name='new_article'),
    url(r'^', include(router.urls)),
]
