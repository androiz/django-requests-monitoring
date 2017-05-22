from django.shortcuts import render
from django.views.generic import TemplateView
from .models import LogEntry
from .utils import charge_plot_data

# Create your views here.


class MonitoringView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MonitoringView, self).get_context_data(**kwargs)
        context['entries'] = LogEntry.objects.order_by('created_at').reverse()[0:20]

        data1, data2 = charge_plot_data()
        context['data1'] = data1
        context['data2'] = data2

        return context
