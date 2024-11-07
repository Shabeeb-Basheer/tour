from django.contrib import admin
from .models import Hotel, HotelImage,Contact, Update, Gallery, HotelEnquiry, Team, HotelAmenities, Banner, HotelAmenitiesCategory, NearPlace, Client, Testimonial, Faq, Meta, HotelCategory, Event, EventPoint, HotelFaq, HotelHighlight, RoomType, Value, Partnership
# Register your models here.

class HotelImageInline(admin.TabularInline):
    model=HotelImage
    extra=1
    
class HotelAmenitiesInline(admin.TabularInline):
    model = HotelAmenities
    extra = 1

class HotelFaqInline(admin.TabularInline):
    model = HotelFaq
    extra = 1

class HotelHighlightInline(admin.TabularInline):
    model = HotelHighlight      
    extra = 1

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1
class EventPointsInline(admin.TabularInline):
    model = EventPoint
    extra = 1
    
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("title",'price',"category",)
    prepopulated_fields = {"slug": ("title",)}
    inlines=[HotelImageInline,HotelAmenitiesInline,HotelFaqInline,HotelHighlightInline,RoomTypeInline]
    
@admin.register(HotelAmenitiesCategory)
class HotelAmenitiesCategory(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("fullname","phone","email",)
    
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title","gallery_type","is_home",)

@admin.register(HotelEnquiry)
class HotelEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'check_in', 'check_out')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(NearPlace)
class NearPlaceAdmin(admin.ModelAdmin):
    list_display = ("title","order","category","is_trending",)
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("title","name","source","hotel","is_active",)
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question",)
    
@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("title","page",)
    
@admin.register(HotelCategory)
class HotelCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title","place","duration",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [EventPointsInline]

@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ("title","description",)
    
@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ("name","company_name",)