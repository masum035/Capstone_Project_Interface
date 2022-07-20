from .models import Video
from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)


class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("video_holder", "caption", "video",)
        widgets = {

        }
