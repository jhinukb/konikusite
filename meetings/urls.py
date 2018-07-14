from django.conf.urls import url, include

from . import views
from meetings.views import MeetingFormPage


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.CellFormPage.as_view(), name="cell_form")
    url(r'^$', MeetingFormPage.as_view(), name="cell_form"),
    url(r'ajax/load_members/', views.load_members, name='ajax_load_members'),
    url(r'workreview/', views.work_review, name='work_review')
    #url(r'^$', views.load_cellNames, name='load')
    # url(r'^(?P<cell_id>[0-9]+)/$', views.load_cellNames, name='detail')
]
