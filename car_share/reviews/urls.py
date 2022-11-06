from django.urls import path
from reviews.views.review_create import CreateReview
from reviews.views.view_reviews import ViewReviews

app_name = 'reviews'

urlpatterns = [
    path('create/', CreateReview.as_view(), name='create_review'),
    path('view/', ViewReviews.as_view(), name='view_reviews')
]
