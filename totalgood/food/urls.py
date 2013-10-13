from django.conf.urls import patterns, include, url

from food.views import chart, home

#from django.contrib.auth.models import User, Group
from food.models import Nutrient

from rest_framework import viewsets, routers

class NutrientViewSet(viewsets.ModelViewSet):
    model = Nutrient

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'nutrients', NutrientViewSet)

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^chart/', chart),
)

# Wire up API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
