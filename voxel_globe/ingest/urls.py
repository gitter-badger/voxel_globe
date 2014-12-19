from django.conf.urls import patterns, url, include
from voxel_globe.ingest import views

urlpatterns = patterns('',
    url(r'^$', views.ingest, name='ingest'),
    url(r'^upload$', views.upload, name="uploadEndpoint"),
    url(r'^ingestFolder$', views.ingestFolder, name="ingestFolder"),

    url(r'^blah$', views.blah, name="blah_del_me"),

#   RESTful end points
    url(r'^rest/', include(views.router.urls)),
)