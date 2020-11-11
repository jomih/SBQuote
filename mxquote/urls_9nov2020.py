from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^pepe/$', views.showmpcnames),
    url(r'^quotemxh/$', views.quotemxh, name='quotemxh'),
    url(r'^result_quote/$', views.result_quote, name='result_quote'),
    url(r'^quotemxl/$', views.quotemxl, name='quotemxl'),
    url(r'^quotempc$', views.quotempc, name='quotempc'),
    url(r'^viewmpc$', views.MPCListView.as_view(), name='viewmpc'),
    url(r'^viewlicense$', views.viewlicense, name='viewlicense'),
    url(r'^viewoptics$', views.viewoptics, name='viewoptics'),
]
