from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home.views.index'),
    url(r'^about/', 'home.views.about'),
    url(r'^sponsors/', 'home.views.sponsors'),
    url(r'^calendar/', 'home.views.calendar'),
    url(r'^events/', 'home.views.events'),
    url(r'^favicon.ico$', lambda x: HttpResponseRedirect(settings.MEDIA_URL+'/favicon.ico')), #google chrome favicon fix
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
