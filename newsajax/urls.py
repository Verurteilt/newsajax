from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',

    url(r'^$', 'newsajax.newsajax.views.index', name='home'),
    url(r'^about/$', 'newsajax.newsajax.views.about', name='about'),
    url(r'^about_author/$', 'newsajax.newsajax.views.about_author', name='about_author'),
    url(r'^contacto/$', 'newsajax.newsajax.views.contacto', name="contacto"),
    url(r'^contacto_ajax/$', 'newsajax.newsajax.views.contacto_ajax'),
    url(r'^login/$', 'newsajax.newsajax.views.login', name="login"),
    url(r'^login_ajax/$', 'newsajax.newsajax.views.login_ajax'),
    url(r'^logout/$', 'newsajax.newsajax.views.logout', name="logout"),
    url(r'^registro/$', 'newsajax.newsajax.views.registro', name="registro"),
    url(r'^registro_ajax/$', 'newsajax.newsajax.views.registro_ajax'),
    url(r'^perfil/(?P<id_usuario>.*)/$', 'newsajax.usuarios.views.perfil_ver', name='perfil'),
    url(r'^editar/(?P<id_usuario>.*)$', 'newsajax.usuarios.views.editar', name="editar"),
    url(r'^ver_noticias/(?P<id_usuario>.*)/page/(?P<pagina>.*)$', 'newsajax.noticias.views.ver_noticias', name="ver_noticias"),
    url(r'^ver/noticia/(?P<id_noticia>.*)$', 'newsajax.noticias.views.ver_noticias_alone', name="ver_noticias_alone"),
    url(r'^eliminar/(?P<id_noticia>.*)$', 'newsajax.noticias.views.eliminar', name="eliminar"),
    url(r'^editar_noticias/(?P<id_noticia>.*)$', 'newsajax.noticias.views.editar', name="editar_noticia"),
    url(r'^editar_noticia_ajax/$', 'newsajax.noticias.views.editar_noticia_ajax'),
    url(r'^editar_ajax/$', 'newsajax.usuarios.views.editar_ajax'),
    url(r'^add/$', 'newsajax.noticias.views.add_notice', name="add"),
    url(r'^add_notice_ajax/$', 'newsajax.noticias.views.add_notice_ajax'),
    # url(r'^newsajax/', include('newsajax.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
