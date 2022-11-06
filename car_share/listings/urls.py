from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from listings.views.create_listing import CreateListing
from listings.views.view_listings import ViewListings
from listings.views.delete_listing import DeleteListing

app_name = 'listings'

urlpatterns = [
    path("listings/create", CreateListing.as_view(), name="create_listing"),
    path("listings/view", ViewListings.as_view(), name="view_listings"),
    path("listings/delete", DeleteListing.as_view(), name="delete_listing")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
