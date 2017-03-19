from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DEL'


class LogEntry(models.Model):

    METHODS = (
        (GET, 'GET'),
        (POST, 'POST'),
        (PUT, 'PUT'),
        (DELETE, 'DELETE')
    )

    ip_address = models.CharField(
        max_length=15,
        blank=True,
        null=False
    )
    user_identifier = models.CharField(
        max_length=100,
        blank=True,
        null=False
    )
    user = models.ForeignKey(
        User,
        related_name='user',
        blank=False,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False
    )
    method = models.CharField(
        max_length=4,
        choices=METHODS,
        blank=False,
        null=False
    )
    path = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    protocol = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    status = models.IntegerField(
        blank=False,
        null=False
    )
    size = models.IntegerField(
        blank=False,
        null=False
    )

    def __unicode__(self):

        return '{} {} {} {} \"{} {} {}\" {} {}'.format(
            self.ip_address,
            self.user_identifier,
            self.user,
            self.created_at,
            self.method,
            self.path,
            self.protocol,
            self.status,
            self.size
        )

    def __str__(self):
        return '{} {} {} {} \"{} {} {}\" {} {}'.format(
            self.ip_address,
            self.user_identifier,
            self.user,
            self.created_at,
            self.method,
            self.path,
            self.protocol,
            self.status,
            self.size
        )