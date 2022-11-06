from django.db import models
from listings.models import ListingsModel
from django.db.models import CASCADE

# Create your models here.


class Review(models.Model):
    score = models.IntegerField(max_length=1)
    listing = models.ForeignKey(ListingsModel, on_delete=CASCADE, related_name="listing")
    review_text = models.TextField(max_length=500, null=True, blank=True)