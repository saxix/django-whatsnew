from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from whatsnew.models import WhatsNew


class ChangelogView(ListView):
    template_name='whatsnew/changelog.html'
    model = WhatsNew

    def get_queryset(self):
        return self.model._default_manager.all().order_by('-version')
