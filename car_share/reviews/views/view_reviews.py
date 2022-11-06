from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from reviews.models import Review


class ViewReviews(View):
    def get(self, request):
        reviews = []
        if request.user.is_authenticated:
            if Review.objects.filter().exists():
                review_set = Review.objects.all()
                for review in review_set:
                    reviews.append({"id": f'{review.id}',
                                    "score": f'{review.score}',
                                    "listing": f'{review.listing}',
                                    "reviewer": f'{review.listing.renter}',
                                    "reviewee": f'{review.listing.owner}',
                                    "text": f'{review.text}'})

                return JsonResponse(reviews, safe=False)
        else:
            return HttpResponse('UNAUTHORIZED', status=401)