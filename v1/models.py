from datetime import datetime

from django.db import models

class TimeStampedModel(models.Model):
    '''
    Abstract base class to give models created at and updated at
    timestamps.
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
