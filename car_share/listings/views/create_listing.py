from django.http import HttpResponseRedirect
from django.views.generic import FormView
from listings.models import ListingsModel
from listings.forms.create_listing_form import CreateListingForm


class CreateListing(FormView):
    template_name = 'listings/create_listing.html'
    form_class = CreateListingForm

    def form_valid(self, form):
        ListingsModel.objects.create(
            location=form.cleaned_data['location'],
            owner=form.cleaned_data['owner'],
            car_type=form.cleaned_data['car_type'],
            gas_percent=form.cleaned_data['gas_percent'],
            mileage=form.cleaned_data['mileage'],
            make_modeln=form.cleaned_data['make_model'],
            renter=form.cleaned_data['renter'],
        )

        return HttpResponseRedirect('accounts/dashboard')
