from django.db import models

# Create your models here.

class Review(models.Model):
    score = models.IntegerField()
    reviewer = models.TextField(max_size=40)
    reviewee = models.TextField(max_size=40)
    review_text = models.TextField(max_size=40)


"""Review:
    score
    reviewer
    reviewee
    text of review
"""

# TODO: add and average out sum for the number of reviews