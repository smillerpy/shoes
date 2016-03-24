from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=30, blank=False)
    address = models.TextField()

    def __unicode__(self):
        return self.name
