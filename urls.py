"""
GAVIP Example AVIS: Simple AVI

These URLs are used by the AVI web-interface.
@req: REQ-0006
@comp: AVI Web System
"""
from avi import views
from avi import views_api
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


api_urls = [
    # API definitions
    url(r'^$', views_api.DemoModelList.as_view(), name='demomodel-list'),
    url(r'^(?P<pk>[0-9]+)/$', views_api.DemoModelDetail.as_view(), name='demomodel-detail'),
]
api_urls = format_suffix_patterns(api_urls)

urlpatterns = patterns(
    '',
    url(r'^$', views.main, name='main'),

    url(r'^api/', include(api_urls, namespace='api')),
    
    url(r'^run_query/$',
        views.run_query, name='run_query'),
    
    url(r'^job_list/$',
        views.job_list, name='job_list'),
    
    url(r'^job_data/(?P<job_id>[0-9]+)/$',
        views.job_data, name='job_data'),

    url(r'^result/(?P<job_id>[0-9]+)/$',
        views.job_result, name='job_result'),
    
    url(r'^public/result/(?P<job_id>[0-9]+)/(?P<celery_task_id>[a-z0-9-]+)/$',
        views.job_result_public, name='job_result_public'),
)

