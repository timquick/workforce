from django.conf.urls import patterns, url, include
from leasing import views

urlpatterns = patterns('',
    url(r'^staff$', views.ListStaff.as_view(), name='staff_list'),
    url(r'^staff/(?P<pk>\d+)$', views.ViewStaff.as_view(), name='staff_detail'),
    url(r'^staff/(?P<pk>\d+)/edit$', views.EditStaff.as_view(), name='staff_update'),
    url(r'^staff/new$', views.NewStaff.as_view(), name='staff_add'),
)
