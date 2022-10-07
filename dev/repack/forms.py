from django import forms
from repack.models import Item
from repack.models import Contact


class ItemRequestForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.FloatField()
    description = forms.Textarea()
    image = forms.ImageField()

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return data

    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'image')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
        }  

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message'}))
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
        }