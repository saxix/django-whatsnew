from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    'whatsnew.views',
    url(r'^test/', TemplateView.as_view(template_name='whatsnew/test.html'), name='whatsnew-test'),
    # url(r'^latest/$', 'latest', name='whatsnew-latest'),
)


