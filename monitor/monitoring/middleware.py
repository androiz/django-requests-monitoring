from .models import LogEntry

from django.contrib.auth.models import User

class MonitoringMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        ip_address = request.META['REMOTE_ADDR']
        # port = request.SERVER_PORT
        # host = request.SERVER_NAME
        # query_string = request.QUERY_STRING
        user_identifier = request.META['USER']
        user = None #request.user if request.user in request else None
        method = request.META['REQUEST_METHOD']
        path = request.META['PATH_INFO']
        protocol = request.META['SERVER_PROTOCOL']

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        status = response.status_code
        size = 0
        log_entry = LogEntry.objects.create(
            ip_address=ip_address,
            user_identifier=user_identifier,
            user=user,
            method=method,
            path=path,
            protocol=protocol,
            status=status,
            size=size
        )

        return response