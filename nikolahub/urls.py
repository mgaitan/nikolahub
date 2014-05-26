from django.conf.urls import patterns, include, url
from django.contrib import admin
from nikolahub.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nikolahub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url('^auth/', include('social.apps.django_app.urls', namespace='social')),
    url('^hook/', include('github_hook.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
