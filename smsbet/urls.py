from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'play.views.webplay', name='web_play'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^download/pins/', 'pins.views.download_pins'),
    url(r'^traffic/$', 'traffiq.views.report'),
    url(r'^emmob/$', 'emmob.views.report'),
    url(r'^map/$', 'traffiq.views.map'),
    url(r'^markers/$', 'traffiq.views.get_markers'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', name='site_login'),
    url(r'^accounts/logout/$', 'logout',
        {'next_page': '/'}, name='site_logout'),
)
