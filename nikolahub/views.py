from django.views.generic.base import TemplateView
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'nikolahub/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

