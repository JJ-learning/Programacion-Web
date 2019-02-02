from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shortcut.views.home', name='home'),

    url(r'^login$', 'shortcut.views.login_view'), # login
    url(r'^user/new$', 'shortcut.views.newUser'), # register
    url(r'^logout$', 'shortcut.views.logout_view'),   # logout
    url(r'^users$', 'shortcut.views.users'), #muestra todos los perfiles
    url(r'^user/(?P<username>\w{0,30})$', 'shortcut.views.users'), #muestra un perfil en particular
    url(r'^interactions$', 'shortcut.views.interactions'), #muestra los tweets que referencian a un usuario
    url(r'^settings$','shortcut.views.settings'), 

    url(r'^submit$', 'shortcut.views.submit'),
    url(r'^shortcuts$', 'shortcut.views.public'), # public 
   url(r'^follow$', 'shortcut.views.follow'),
   url(r'^search$', 'shortcut.views.search_view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
