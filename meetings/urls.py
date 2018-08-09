from django.conf.urls import url, include

from . import views
from meetings.views import MeetingFormPage, WorkReviewPage, ObjectivePage


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.CellFormPage.as_view(), name="cell_form")
    url(r'^$', MeetingFormPage.as_view(), name="cell_form"),
    url(r'ajax/load_members/', views.load_members, name='ajax_load_members'),
    url(r'^workreview/$', WorkReviewPage.as_view(), name='work_review'),
    url(r'objectives/', ObjectivePage.as_view(), name='objectives'),
    url(r'objectives_review/', views.objective_review, name='objectives_review')
    # url(r'obj_review_page/', ObjectiveReviewPage.as_view(), name='obj_review_page')
    #url(r'^$', views.load_cellNames, name='load')
    # url(r'^(?P<cell_id>[0-9]+)/$', views.load_cellNames, name='detail')
]
