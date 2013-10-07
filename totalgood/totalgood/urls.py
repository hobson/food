from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'totalgood.views.home', name='home'),
    url(r'^food/', include('totalgood.food.urls')),
    # url(r'^chart/', include('totalgood.chart.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


#from django.contrib.auth.models import User, Group
from food.models import Vitamin

from rest_framework import viewsets, routers

class VitaminViewSet(viewsets.ModelViewSet):
    model = Vitamin

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'jobs', VitaminViewSet)

# Wire up API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

