from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import os
site_media = os.path.join(
    os.path.dirname(__file__),  'site_media'
) 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plataforma.views.home', name='home'),
    # url(r'^plataforma/', include('plataforma.foo.urls')),
    url(r'^$', 'archivos.views.index', name='inicio'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^archivos/$', 'archivos.views.index'),
    (r'^archivos/add$', 'archivos.views.add'),
    (r'^archivos/select_ajax$', 'archivos.views.select_ajax'),

    (r'^login$', 'usuarios.views.login'),
    (r'^salir$', 'usuarios.views.logout_view'),
    (r'^registro$', 'usuarios.views.registro'),
    
    (r'^buzon$', 'correos.views.index'),
    (r'^buzon/out$', 'correos.views.out'),
    (r'^buzon/componer$', 'correos.views.componer'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': site_media}),

    url(r'^chaining/', include('smart_selects.urls')),
)
