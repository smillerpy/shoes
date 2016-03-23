from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    total_in_shelf = models.IntegerField()
    total_in_vault = models.IntegerField()
    store = models.ForeignKey("store.Store")
