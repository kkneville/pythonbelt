from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),

    url(r'^addquote$', views.addquote, name="addquote"),
    url(r'^addfav$', views.addfav, name="addfav"),
    url(r'^removefav$', views.removefav, name="removefav"),

    url(r'^(?P<id>\d+)/showmember$', views.showmember, name="showmember"),

    url(r'^logout$', views.logout, name="logout"),
]
