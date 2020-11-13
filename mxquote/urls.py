from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^pepe/$', views.showmpcnames),
    url(r'^quotemx960/$', views.quotemx960, name='quotemx960'),
    url(r'^quotemxh/$', views.quotemxh, name='quotemxh'),
    url(r'^make_quote/$', views.make_quote, name='make_quote'),
    url(r'^result_quote/$', views.result_quote, name='result_quote'),
    url(r'^quotemxl/$', views.quotemxl, name='quotemxl'),
    url(r'^quotempc$', views.quotempc, name='quotempc'),
    url(r'^viewmpc$', views.MPCListView.as_view(), name='viewmpc'),
    url(r'^viewmic$', views.MICListView.as_view(), name='viewmic'),
    url(r'^viewsbc$', views.SCBListView.as_view(), name='viewsbc'),
    url(r'^viewre$', views.REListView.as_view(), name='viewre'),
    url(r'^viewlicense$', views.LicenseListView.as_view(), name='viewlicense'),
    url(r'^viewoptics$', views.viewoptics, name='viewoptics'),
]
