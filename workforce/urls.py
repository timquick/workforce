from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workforce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^leasing/', include('leasing.urls')),
    url(r'^people/', include('people.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'thirdauth.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
