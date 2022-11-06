from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from listings.models import ListingsModel
from reviews.models import Review


class ViewListings(View):
    def get(self, request):
        listings = []
        if request.user.is_authenticated:
            if ListingsModel.objects.filter(renter='').exists():
                listing_set = ListingsModel.objects.filter(renter='')
                owners_scores = {}

                for listing in listing_set:

                    owner = listing.owner
                    if owner in owners_scores:
                        overall_score = owners_scores[owner]
                    else:
                        number_of_times_reviewed = Review.objects.filter(reviewee=f'{owner}').count()
                        reviews = Review.objects.filter(reviewee=f'{owner}')
                        total_score = 0
                        for review in reviews:
                            total_score += review.score
                        overall_score = round((total_score / number_of_times_reviewed), 2)

                    listings.append({"id": f'{listing.id}',
                                     "location": f'{listing.location}',
                                     "owner": f'{listing.owner}',
                                     "car_type": f'{listing.car_type}',
                                     "gas_percent": f'{listing.gas_percent}',
                                     "mileage": f'{listing.mileage}',
                                     "make_model": f'{listing.make_model}',
                                     f"reviewer_score": f'{overall_score}'})

                return JsonResponse(listings, safe=False)
        else:
            return HttpResponse('UNAUTHORIZED', status=401)