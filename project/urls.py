from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from welcome.views import LandingView,StreamView
from django.conf.urls import url
from django.conf import settings


#from welcome.views import index, health


#rest framework
from rest_framework import routers, serializers, viewsets

from django.conf.urls import handler404

# Serializers define the API representation.


# ViewSets define the view behavior.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('stream', StreamView)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  #rest_framework
    url(r'^home/(?P<slugcatergory>.*)/$', LandingView),	
    url(r'^$', TemplateView.as_view(template_name = 'index.html')),
    url(r'^health$', health),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^contact', TemplateView.as_view(template_name = 'contact.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
