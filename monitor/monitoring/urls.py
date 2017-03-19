from django.conf.urls import url
from .views import MonitoringView

urlpatterns = [
    url(r'^', MonitoringView.as_view(), name='monitoring'),
]