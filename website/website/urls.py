from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
    url(r'^about/', 'home.views.about'),
    url(r'^sponsors/', 'home.views.sponsors'),
    url(r'^calendar/', 'home.views.calendar'),
    url(r'^officers/', 'home.views.officers'),
    url(r'^wais/', 'home.views.wais'),
    url(r'^events/$', 'home.views.events'),
    url(r'^twitter/$', 'home.views.twitter'),
    url(r'^events/admin', 'home.views.event_admin'),
    url(r'^newsletter/(?P<id>[0-9]{4}-[0-9]{1,2})/$', 'home.views.newsletter'),
    url(r'^newsletter/', 'home.views.newsletter_home'),
    #google chrome favicon fix; https://gist.github.com/iepathos/5350503
    url(r'^favicon.ico$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'favicon.ico')),
    # CAS (see django_cas_ng)
    url(r'^login/', 'django_cas_ng.views.login'),
    url(r'^logout/', 'django_cas_ng.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'home.views.error500'