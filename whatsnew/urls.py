from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from whatsnew.views import ChangelogView


urlpatterns = patterns(
    'whatsnew.views',
    url(r'^test/', TemplateView.as_view(template_name='whatsnew/test.html'),
        name='whatsnew-test'),
    url(r'^changelog/', ChangelogView.as_view(),
        name='whatsnew-changelog'),
    # url(r'^latest/$', 'latest', name='whatsnew-latest'),
)
