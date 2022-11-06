from django.http import HttpResponseRedirect
from django.views.generic import FormView
from reviews.models import Review
from reviews.forms.create_review_form import CreateReviewForm


class CreateReview(FormView):
    template_name = 'reviews/create_review.html'
    form_class = CreateReviewForm

    def form_valid(self, form):
        Review.objects.create(
            score=form.cleaned_data['score'],
            listing=form.cleaned_data['listing'],
            review_text=form.cleaned_data['review_text'],
        )

        return HttpResponseRedirect('accounts/dashboard')
