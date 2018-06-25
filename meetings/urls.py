from django.conf.urls import url, include

from . import views
from meetings.views import CellFormPage


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.CellFormPage.as_view(), name="cell_form")
    url(r'^$', CellFormPage.as_view(), name="cell_form")
    #url(r'^$', views.load_cellNames, name='load')
    # url(r'^(?P<cell_id>[0-9]+)/$', views.load_cellNames, name='detail')
]
