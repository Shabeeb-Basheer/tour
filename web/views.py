from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Facility, NearPlace, HotelImage, Update, Gallery, HotelPrice, Team, HotelAmenities, Banner, HotelAmenitiesCategory, Client, Testimonial, Faq, Meta, Event, HotelCategory, Value
from .forms import ContactForm, RoomEnquiryForm, RoomEnquiryBaseForm, PartnershipForm, ReviewForm
from django.http import JsonResponse
import calendar
from .utils import PackageCalendar
from datetime import datetime, timedelta, date
from django.core.mail import send_mail
import urllib.parse
from urllib.parse import quote

# Create your views here.
def index(request):
    hotel_categories = HotelCategory.objects.all()
    hotel_lists=Hotel.objects.all()[:3]
    facilities = Facility.objects.all()
    midpoint = len(facilities) // 2 
    banners = Banner.objects.all()
    gallery_images = Gallery.objects.filter(gallery_type="image_gallery",is_home="True")[:6]
    updates = Update.objects.all()[:3]
    partners = Client.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    meta = Meta.objects.filter(page="home").first()
    near_places = NearPlace.objects.filter(is_trending=True)

    context={
        "is_index":True,
        "hotel_categories":hotel_categories,
        'hotel_lists':hotel_lists,
        'facilities':facilities,
        "midpoint":midpoint,
        "banners":banners,
        "gallery_images":gallery_images,
        "updates":updates,
        "partners":partners,
        "testimonials":testimonials,
        "meta":meta,
        "near_places":near_places
        
    }
    return render(request,'web/index.html',context)


def about_us(request):
    teams = Team.objects.all()
    facilities = Facility.objects.all()
    faqs = Faq.objects.all()
    meta = Meta.objects.filter(page="about").first()
    testimonials = Testimonial.objects.filter(is_active=True)
    partners = Client.objects.all()
    values = Value.objects.all()
    
    context = {
        "is_about":True,
        "teams":teams,
        "facilities":facilities,
        "faqs":faqs,
        "meta":meta,
        "testimonials":testimonials,
        "partners":partners,
        "values":values
    }
    return render(request,"web/about.html",context)


def update(request):
    updates = Update.objects.all()
    meta = Meta.objects.filter(page="updates").first()

    context = {
        "is_updates":True,
        "updates":updates,
        "meta":meta
    }
    return render(request,"web/update.html",context)


def update_detail(requets,slug):
    update = get_object_or_404(Update, slug=slug)
    other_updates = Update.objects.exclude(slug=slug)

    context = {
        "update":update,
        "other_updates":other_updates,
        
    }
    return render(requets,"web/update-details.html",context)


def contact(request):
    meta = Meta.objects.filter(page="contact_us").first()
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            data = contact.save(commit=False)
            data.save()
            
            # Send email notification
            subject = "Contact Enquiry Information"
            message = (
                f'Name: {data.fullname} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Message: {data.message}\n'
            )
            from_email = "greenleavesholiday@gmail.com"
            recipient_list = ["greenleavesholiday@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            # Prepare WhatsApp message
            whatsapp_message = (
                f'Name: {data.fullname} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Message: {data.message}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943888500"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            
            # Redirect to WhatsApp
            return redirect(whatsapp_url)
        else:
            # Handle form validation errors
            error_messages = {field: contact.errors[field][0] for field in contact.errors}
            print("Form Validation Error:", error_messages)  # Log the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
            return JsonResponse(response_data)
    else:
        contact = ContactForm()
        context = {"contact": contact, "meta": meta, "is_contact": True,}
        return render(request, 'web/contact.html', context)
    
    
def hotel_list(request,slug):
    meta = Meta.objects.filter(page="hotels").first()
    category = get_object_or_404(HotelCategory, slug=slug)
    hotels = Hotel.objects.filter(category=category)
    near_places = NearPlace.objects.filter(category=category)

    context = {
        "is_hotels":True,
        "hotels":hotels,
        "meta":meta,
        "near_places": near_places,
        
    }
    return render(request,"web/hotel-list.html",context)


def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    amenity_categories = HotelAmenitiesCategory.objects.all()
    amenities_content = HotelAmenities.objects.filter(hotel=hotel)
    slide_images = HotelImage.objects.filter(hotel=hotel)
    facilities = HotelAmenities.objects.filter(hotel=hotel)
    facility_categories = HotelAmenitiesCategory.objects.all()
    hotel_prices = HotelPrice.objects.filter(hotel=hotel)
    d = get_date(request.GET.get('month', None))
    user = request.user
    cal = PackageCalendar(d.year, d.month, hotel, user)
    html_cal = cal.formatmonth(withyear=True)
    testimonials = Testimonial.objects.filter(hotel=hotel,is_active=True)
    near_places = NearPlace.objects.filter(category=hotel.category)[:6]  # Adjusted near_places filter
    
    if request.method == "POST":
        form = RoomEnquiryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.hotel = hotel
            data.save()
            
            # Send email notification
            subject = "Room Enquiry Information"
            message = (
                f"Enquiry for: {data.hotel} \n"
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Check In: {data.check_in}\n'
                f'Check Out: {data.check_out}\n'
                f'Adults: {data.adult}\n'
                f'Children: {data.children}\n'
            )
            from_email = "greenleavesholiday@gmail.com"  # Update with your email
            recipient_list = ["greenleavesholiday@gmail.com"]  # Update with recipient's email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            # Prepare WhatsApp message
            whatsapp_message = (
                f"Enquiry for: {data.hotel} \n"
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Check In: {data.check_in}\n'
                f'Check Out: {data.check_out}\n'
                f'Adults: {data.adult}\n'
                f'Children: {data.children}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943888500"  # Update with your WhatsApp number
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            
            # Redirect to WhatsApp
            return redirect(whatsapp_url)
        else:
            # Handle form validation errors
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  # Log the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
            return JsonResponse(response_data)
    else:
        form = RoomEnquiryForm()
    
    context = {
        "is_room": True,
        "hotel": hotel,
        "calendar_html": html_cal,
        "prev_month": prev_month(d),  # Ensure prev_month and next_month functions are defined
        "next_month": next_month(d),
        "form": form,
        "slide_images": slide_images,
        "hotel_prices": hotel_prices,
        "facilities": facilities,
        "facility_categories": facility_categories,
        "testimonials": testimonials,
        "near_places": near_places,
        "amenities_content":amenities_content,
        "amenity_categories":amenity_categories
    }
    return render(request, "web/hotel-detail.html", context)


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def ajax_load_date_based_price(request):
    selected_date = request.GET.get('selected_date')
    package_id = request.GET.get('package_id')
    
    try:
        package = get_object_or_404(Hotel, pk=package_id)
        price = HotelPrice.objects.filter(package=package, package_date=selected_date).first()
        
        if price:
            response_data = {
                'success': True,
                'price': price.rate,
            }
        else:
            response_data = {
                'success': False,
                'message': 'Selected date Already Booked ,Try Another Date..',
            }
    except Exception as e:
        response_data = {
            'success': False,
            'message': str(e),
        }

    return JsonResponse(response_data)   

def image_gallery(request):
    meta = Meta.objects.filter(page="image_gallery").first()
    galleries = Gallery.objects.filter(gallery_type="image_gallery")

    context = {
        "is_gallery":True,
        "is_image_gallery":True,
        "galleries": galleries,
        "meta":meta
    }
    print(context)  # Debugging: Print context to check its content
    return render(request, "web/image_gallery.html", context)


def video_gallery(request):
    meta = Meta.objects.filter(page="video_gallery").first()
    galleries = Gallery.objects.filter(gallery_type="video_gallery")

    context = {
        "is_video_gallery":True,
        "galleries": galleries,
        "meta":meta
    }
    print(context)  # Debugging: Print context to check its content
    return render(request, "web/video_gallery.html", context)


def booking_enquiry(request):
    if request.method == "POST":
        form = RoomEnquiryBaseForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # Assign a specific hotel instance
            data.hotel = form.cleaned_data['hotel']
            data.save()
            
            # Send email notification
            subject = "Room Enquiry Information"
            message = (
                f"Enquiry for: {data.hotel.title} \n"
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Check In: {data.check_in}\n'
                f'Check Out: {data.check_out}\n'
                f'Adults: {data.adult}\n'
                f'Children: {data.children}\n'
            )
            from_email = "greenleavesholiday@gmail.com"
            recipient_list = ["greenleavesholiday@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            # Prepare WhatsApp message
            whatsapp_message = (
                f"Enquiry for: {data.hotel.title} \n"
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Check In: {data.check_in}\n'
                f'Check Out: {data.check_out}\n'
                f'Adults: {data.adult}\n'
                f'Children: {data.children}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943888500"
            encoded_message = quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            
            # Redirect to WhatsApp
            return redirect(whatsapp_url)
        else:
            # Handle form validation errors
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  # Log the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
            return JsonResponse(response_data)
    else:
        form = RoomEnquiryBaseForm()
    return render(request, 'enquiry_form.html', {'form': form})
   
   
def event(request):
    meta = Meta.objects.filter(page="events").first()
    events = Event.objects.all()
    context = {
        "is_event": True,
        "meta":meta,
        "events":events
    }
    return render(request, "web/event.html", context)


def event_detail(request,slug):
    event = Event.objects.get(slug=slug)
    context = {
        "event": event,
    }
    return render(request, "web/event-detail.html", context)


def sightseeing_place(request):
    near_places = NearPlace.objects.all()
    meta = Meta.objects.filter(page="nearby_place").first()
    context = {
        "near_places":near_places,
        "meta":meta
    }
    return render(request,"web/sightseeing-place.html",context)

    
def review_enquiry(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST,  request.FILES)
        if review_form.is_valid():
            review_form.save()
            response_data = {
                "is_contact": True,
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Your Review is Submitted",
            }
        else:
            error_messages = {field: review_form.errors[field][0] for field in review_form.errors}
            print("Form Validation Error:", error_messages)  # Print the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
        return JsonResponse(response_data)
    else:
        review_form = ContactForm()
        context = {"review_form": review_form, "is_contact": True}
    return render(request, "enquiry_form.html", context)


def partnership_enquiry(request):
    if request.method == "POST":
        partnership_form = PartnershipForm(request.POST)
        if partnership_form.is_valid():
            data = partnership_form.save(commit=False)
            data.save()

            # Send email notification
            subject = "Partnership Enquiry"
            message = (
                f"Enquiry from: {data.company_name}\n"
                f'Name: {data.name}\n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Company: {data.company_name}\n'
                f'Proposal: {data.proposal_description}\n'
            )
            from_email = "greenleavesholiday@gmail.com"
            recipient_list = ["greenleavesholiday@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Prepare WhatsApp message
            whatsapp_message = (
                f"Enquiry from: {data.company_name}\n"
                f'Name: {data.name}\n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Company: {data.company_name}\n'
                f'Proposal: {data.proposal_description}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943888500"
            encoded_message = quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Return a JSON response with the WhatsApp URL
            return redirect(whatsapp_url)

        else:
            # Handle form validation errors
            error_messages = {field: partnership_form.errors[field][0] for field in partnership_form.errors}
            return JsonResponse({"status": "error", "title": "Form Validation Error", "message": error_messages})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

def handler404(request, exception):
    return render(request, "web/404.html", status=404)
