
from django.urls import path
from django.views.generic import TemplateView
from .import views

app_name="web"

urlpatterns = [
  path('',views.index,name="index"),
  path('about_us/',views.about_us,name="about_us"),
  path("hotel/hotel-list/<slug:slug>/",views.hotel_list,name="hotel_list"),
  path("hotel/<slug:slug>/", views.hotel_detail, name="hotel_detail"),
  path("image-gallery/",views.image_gallery,name="image_gallery"),
  path("video-gallery/",views.video_gallery,name="video_gallery"),
  path("event/",views.event,name='event'),
  path("event-detail/<slug:slug>/",views.event_detail,name="event_detail"),
  path("update/",views.update,name='update'),
  path("update-detail/<slug:slug>/",views.update_detail,name="update_detail"),
  path("contact/",views.contact,name='contact'),
  path("booking-enquiry/",views.booking_enquiry,name="booking_enquiry"),
  path("partnership-enquiry/",views.partnership_enquiry,name="partnership_enquiry"),
  path("review-enquiry/",views.review_enquiry,name="review_enquiry"),
  path("sightseeing-place/",views.sightseeing_place,name="sightseeing_place"),
  path("privacy-policy/", TemplateView.as_view(template_name="web/privacy-policy.html"),name='privacy-policy'),
]