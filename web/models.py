from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField  
from django.utils.text import slugify
# Create your models here.

class HotelCategory(models.Model):
    order = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True,null=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Hotel Category'
        verbose_name_plural = 'Hotel Categories'
        
    def get_absolute_url(self):
        return reverse_lazy('web:hotel_list', kwargs={'slug': self.slug})
    
    def get_hotels(self):
        return Hotel.objects.filter(category=self)

    def __str__(self):
        return str(self.title)

class Hotel(models.Model):
    category = models.ForeignKey("web.HotelCategory",on_delete=models.CASCADE,blank=True,null=True)
    order = models.IntegerField(unique=True)
    title=models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True, null=True)
    description=models.TextField()
    image = models.ImageField(upload_to="hotel/",blank=True,null=True)
    price=models.IntegerField()
    per = models.CharField(max_length=100,blank=True,null=True)
    place = models.CharField(max_length=100,blank=True,null=True)
    location_url = models.TextField(blank=True,null=True)
    room_capacity = models.CharField(max_length=180,blank=True,null=True)
    meals = models.CharField(max_length=180,blank=True,null=True)
    guest_capasity = models.CharField(max_length=180,blank=True,null=True)
    bathroom_capasity = models.CharField(max_length=180,blank=True,null=True)

    class Meta:
        ordering=('order',)
        verbose_name = ('Hotel')
        verbose_name_plural = ('Hotels')
    
    def get_absolute_url(self):
        return reverse_lazy("web:hotel_detail", kwargs={"slug": self.slug})
    
    def get_hotel_image(self):
        return HotelImage.objects.filter(hotel=self)
    
    def get_hotels(self):
        return HotelCategory.objects.filter(category=self)
    
    def get_hotel_faq(self):
        return HotelFaq.objects.filter(hotel=self)
    
    def get_space_image(self):
        return HotelImage.objects.filter(hotel=self,is_space=True)
    
    def get_hotel_highlights(self):
        return HotelHighlight.objects.filter(hotel=self)
    
    def get_room_type(self):
        return RoomType.objects.filter(hotel=self)
    
    def __str__(self):
        return str(self.title)


class HotelImage(models.Model):
    hotel=models.ForeignKey("web.Hotel",on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Hotel-images/')
    title = models.CharField(max_length=180,blank=True,null=True)
    is_space = models.BooleanField(default=False)

    class Meta:
        ordering=('id',)
        verbose_name = ('Hotel Image')
        verbose_name_plural = ('Hotel Images')


class HotelAmenitiesCategory(models.Model):
    icon = models.ImageField(upload_to="icon/",max_length=180,blank=True,null=True)
    title = models.CharField(max_length=180)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Hotel Amenities Category'
        verbose_name_plural = 'Hotel Amenities Categories'


class HotelAmenities(models.Model):
    category = models.ForeignKey("web.HotelAmenitiesCategory", on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE)
    icon = models.FileField(upload_to="amenities_icon/",blank=True,null=True)
    title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'
    
    def __str__(self):
        return self.title
    

class HotelFaq(models.Model):
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE)
    question = models.CharField(max_length=180)
    answer = models.TextField()
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Faq '
        verbose_name_plural = 'Faqs'
    
    def __str__(self):
        return self.question
    

class HotelHighlight(models.Model):
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Hotel Highlight '
        verbose_name_plural = 'Hotel Highlights'
    
    def __str__(self):
        return self.title
    
class RoomType(models.Model):
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    description =models.TextField()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Types of Room'
        verbose_name_plural = 'Types of Rooms'

    def __str__(self):
        return self.title


class Facility(models.Model):
    image=models.ImageField(upload_to='Facility/')
    title=models.CharField(max_length=50)

    class Meta:
        ordering=('id',)
        verbose_name = ('Facility')
        verbose_name_plural = ('Facilities')
    
    def get_absolute_url(self):
        return reverse_lazy("web:facility_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
        

class NearPlace(models.Model):
    category = models.ForeignKey("web.HotelCategory",on_delete=models.CASCADE,blank=True,null=True)
    order = models.IntegerField(unique=True)
    title=models.CharField(max_length=200)
    sub_title = models.CharField(max_length=240, blank=True, null=True)
    point_1 = models.CharField(max_length=180,blank=True,null=True)
    point_2 = models.CharField(max_length=180,blank=True,null=True)
    image = models.ImageField(upload_to="near_place/",blank=True,null=True)
    place = models.CharField(max_length=200,blank=True,null=True)
    kilometer = models.CharField(max_length=100,blank=True,null=True)
    location = models.URLField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    offer_price = models.IntegerField(blank=True,null=True)
    is_trending = models.BooleanField(default=False)
   

    class Meta:
        ordering=('order',)
        verbose_name = ('Near Place')
        verbose_name_plural = ('Near Places')
    
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(max_length=200)
    message = models.TextField()

    class Meta:
        ordering=('id',)
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __str__(self):
        return self.fullname


class Update(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    auther = models.CharField(max_length=180)
    description = models.TextField()
    image = models.ImageField(upload_to="Update/")

    def get_absolute_url(self):
        return reverse_lazy("web:update_detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering=('id',)
        verbose_name = ('Update')
        verbose_name_plural = ('Updates')
    
    def __str__(self):
        return self.title


class Gallery(models.Model):
    GALLERYTYPE = (
        ('image_gallery', "Image Gallery"),
        ('video_gallery', "Video Gallery")
    )
    gallery_type = models.CharField(max_length=20, choices=GALLERYTYPE, default='image_gallery')
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    is_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title
    
    
class HotelEnquiry(models.Model):
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE, related_name="enquiries")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    adult = models.IntegerField()
    children = models.IntegerField()
    class Meta:
        ordering = ('id',)
        verbose_name = "Hotel Enquiry"
        verbose_name_plural = "Hotel Enquiries"

    def __str__(self):
        return f"Enquiry by {self.name} for {self.hotel}"


class HotelPrice(models.Model):
    PACKAGESTATUS = (('Available', "Available"), ('Booked', "Booked"))
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    package_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=PACKAGESTATUS, default='Available')

    class Meta:
        ordering = ('id',)
        verbose_name = "Hotel Availability"
        verbose_name_plural = "Hotel Availability"

    def __str__(self):
        return str(self.hotel)
    @property
    def get_html_url(self):
        return f'<a href="javascript:void(0)"> {self.status} </a>'


class Team(models.Model):
    name = models.CharField(max_length=180)
    position = models.CharField(max_length=180)
    image = models.ImageField(upload_to="team/")
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Our Team"
        verbose_name_plural = "Our Teams"
    
    def __str__(self):
        return self.name

    
class Banner(models.Model):
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="banner/")
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Banner" 
        verbose_name_plural = "Banners"
    
    def __str__(self):
        return self.title
    
    
class Client(models.Model):
    hotel = models.ForeignKey("web.Hotel", on_delete=models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="client_logos/")
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Partner" 
        verbose_name_plural = "Partners"
        
    def get_hotel_detail_url(self):
        if self.hotel:
            return reverse_lazy('web:hotel_detail', kwargs={'slug': self.hotel.slug})
        return '#' 
    
    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=180)
    content = models.TextField()
    name = models.CharField(max_length=180)
    source = models.CharField(max_length=180,blank=True,null=True)
    logo = models.FileField(upload_to="testimonial-logo/",blank=True,null=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Customer Review" 
        verbose_name_plural = "Customer Reviews"
    
    def __str__(self):
        return self.title
    

class Faq(models.Model):
    question = models.CharField(max_length=180)
    answer = models.TextField()
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Faq" 
        verbose_name_plural = "Faqs"
    
    def __str__(self):
        return self.question
    

class Meta(models.Model):
    PAGES = (
        ('home', "Home"),
        ('about', "About"),
        ('hotels', "Hotels"),
        ('image_gallery', "Image Gallery"),
        ('video_gallery', "Video Gallery"),
        ('nearby_place', "Nearby Place"),
        ('events', "Events"),
        ('updates', "Updates"),
        ('contact_us', "Contact Us"),
        
    )
    page = models.CharField(max_length=20, choices=PAGES,)
    title = models.CharField(max_length=60)
    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=180)
    url = models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to="meta_image/")
    
    class Meta:
        ordering = ('-id',)
        verbose_name = "Meta" 
        verbose_name_plural = "Metas"
    
    def __str__(self):
        return self.title


class Event(models.Model): 
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    sub_title = models.CharField(max_length=180)
    description = HTMLField()
    image = models.ImageField(upload_to="event/")
    place = models.CharField(max_length=180)
    duration = models.CharField(max_length=180)
    date_time = models.DateTimeField()
    price = models.IntegerField(blank=True,null=True)
    offer_price = models.IntegerField(blank=True,null=True)
    point = models.CharField(max_length=180,blank=True,null=True)
    point_2 = models.CharField(max_length=180,blank=True,null=True)
    
    def get_absolute_url(self):
        return reverse_lazy("web:event_detail", kwargs={"slug": self.slug})
    
    def get_event_points(self):
        return EventPoint.objects.filter(event=self)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Event" 
        verbose_name_plural = "Events"
        
    def __str__(self):
        return self.title
    
    
class EventPoint(models.Model):
    event = models.ForeignKey("web.Event", on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Event Point" 
        verbose_name_plural = "Event Points"
        
    def __str__(self):
        return self.title
    
    
class Value(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()

    class Meta:
        ordering = ("id",)
        verbose_name = 'Value'
        verbose_name_plural = 'Values'

    def __str__(self):
        return self.title
    
    
class Partnership(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=180)
    company_name = models.CharField(max_length=180)
    proposal_description = models.TextField()

    class Meta:
        ordering = ("id",)
        verbose_name = 'Partnership'
        verbose_name_plural = 'Partnerships'

    def __str__(self):
        return self.name
        