from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import MonitoringView

urlpatterns = [
    url(r'^', login_required(MonitoringView.as_view()), name='monitoring'),
]