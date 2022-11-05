from django.db import models

# Create your models here.

class ReviewModel(models.Model):
    # foreign_key = # get tihs from user models
    score = models.IntegerField() 
    reviewer = models.TextField()
    reviewee = models.TextField()
    review_text = models.TextField()

# TODO: add and average out sum for the number of reviews