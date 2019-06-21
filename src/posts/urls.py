from django.conf.urls import include,url
from django.contrib import admin
from posts import views as post_views

urlpatterns = [
    url(r'^posts/$', post_views.post_home),
#    url(r'^posts/$', 'posts.views.post_home'), this way is no longer supported

    url(r'^create/$', post_views.post_create),
    url(r'^detail/$', post_views.post_detail),
    url(r'^list/$', post_views.post_list),
    url(r'^update/$', post_views.post_update),
    url(r'^delete/$', post_views.post_delete),


]