from django.urls import re_path as url
from django.conf.urls import include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'variants', views.VariantViewSet)
router.register(r'genes', views.GeneViewSet)
router.register(r'aa-changes', views.AminoAcidChangeViewSet)
router.register(r'alfa', views.AlfaDataViewSet)
router.register(r'aa-annotations', views.AminoAcidAnnotationViewSet)
router.register(r'gene-annotations', views.GeneAnnotationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/search/(?P<search_term>[0-9A-Za-z_\-]+)/$', views.search, name='api_search'),
]
