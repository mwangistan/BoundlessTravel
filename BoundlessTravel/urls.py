from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'boundless.views.main'),
                       url(r'^blog/$', 'boundless.views.posts'),
                       url(r'^blog/(?P<pk>\d+)/$', 'boundless.views.detail'),
                       (r'^ckeditor/', include('ckeditor.urls')),
                      
                     
                       
    # Examples:
    # url(r'^$', 'BoundlessTravel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
