from django import forms

from .models import Contact, HotelEnquiry, Hotel, Partnership, Testimonial


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "fullname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Enter Your Email:",
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Enter Your Number:",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Your Message:",
                }
            ),
        }
    

class RoomEnquiryForm(forms.ModelForm):
    class Meta:
        model = HotelEnquiry
        exclude = ("hotel",)
        widgets = {
            "name": forms.widgets.TextInput(attrs={"class": "required form-control input", "placeholder": "Your Name", "required": True}),
            "phone": forms.widgets.TextInput(attrs={"class": "required form-control input", "placeholder": "Your Number", "required": True}),
            "email": forms.widgets.EmailInput(attrs={"class": "required form-control input", "placeholder": "Your Email Address", "required": True}),
            "check_in": forms.widgets.DateInput(attrs={"class": "required form-control input datepicker", "placeholder": "Check In", "required": True, "type": "date", "autocomplete": "off"}),
            "check_out": forms.widgets.DateInput(attrs={"class": "required form-control input datepicker", "placeholder": "Check Out", "required": True, "type": "date", "autocomplete": "off"}),
            "adult": forms.widgets.NumberInput(attrs={"class": "required form-control input", "placeholder": "Adults", "required": True}),
            "children": forms.widgets.NumberInput(attrs={"class": "required form-control input", "placeholder": "Children", "required": True}),
        }
        
class RoomEnquiryBaseForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), widget=forms.Select(attrs={"class": "required form-control input", "required": True}))

    class Meta:
        model = HotelEnquiry
        exclude = ("id",)
        widgets = {
            "name": forms.widgets.TextInput(attrs={"class": "required form-control input", "placeholder": "Your Name", "required": True}),
            "phone": forms.widgets.TextInput(attrs={"class": "required form-control input", "placeholder": "Your Number", "required": True}),
            "email": forms.widgets.EmailInput(attrs={"class": "required form-control input", "placeholder": "Your Email Address", "required": True}),
            "adult": forms.widgets.NumberInput(attrs={"class": "required form-control input", "placeholder": "Adults", "required": True}),
            "children": forms.widgets.NumberInput(attrs={"class": "required form-control input", "placeholder": "Children", "required": True}),
            "check_in": forms.widgets.DateInput(attrs={"class": "required form-control input datepicker", "placeholder": "Check In", "required": True,  "autocomplete": "off", "onfocus": "(this.type='date')", "onblur": "(this.type='text')"}),
            "check_out": forms.widgets.DateInput(attrs={"class": "required form-control input datepicker", "placeholder": "Check Out", "required": True,  "autocomplete": "off","onfocus": "(this.type='date')", "onblur": "(this.type='text')" }),
        }


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control input text-black',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control input',
                'placeholder': 'Enter your email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control input',
                'placeholder': 'Enter your phone number'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control input',
                'placeholder': 'Enter your company name'
            }),
            'proposal_description': forms.Textarea(attrs={
                'class': 'form-control input',
                'rows': 3,
                'placeholder': 'Brief Description of Your Proposal'
            }),
        }
        
        
class ReviewForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(
        queryset=Hotel.objects.all(), 
        widget=forms.Select(attrs={"class": "required form-control input", "required": True})
    )

    class Meta:
        model = Testimonial
        fields = ['hotel', 'name', 'source', 'title', 'content']
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "required form-control input", 
                "placeholder": "Your Name", 
                "required": True
            }),
            "source": forms.TextInput(attrs={
                "class": "form-control input", 
                "placeholder": "Source", 
                "required": False
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control", 
                "placeholder": "Your Review", 
                "required": True
            }),
            "title": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Review Title", 
                "required": True
            }),
        }