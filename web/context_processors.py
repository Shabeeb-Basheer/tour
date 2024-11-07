from .models import HotelCategory
from .forms import RoomEnquiryBaseForm, PartnershipForm, ReviewForm

def header_hotel_categories(request):
    categories = HotelCategory.objects.all().order_by('order')
    return {'header_hotel_categories': categories}


def booking_enquiry_context(request):
    form = RoomEnquiryBaseForm()
    return {
        "form":form
    }


def partnership_enquiry_context(request):
    partnership_form = PartnershipForm()
    return {
        "partnership_form": partnership_form
    }


def review_enquiry_context(request):
    review_form = ReviewForm()
    return {
        "review_form": review_form
    }