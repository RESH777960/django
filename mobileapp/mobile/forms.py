from django.forms import ModelForm
from django import forms



from .models import Product,Brand


class BrandCreateFrom(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"

class ProductCreateFrom(forms.ModelForm):
    class Meta:
        model=Product
        fields = "__all__"
    def clean(self):
            print("insideclean")
            cleaned_data=super().clean()
            price=cleaned_data.get("price")
            if int(price)<500:
                msg = "invalid price"
                return self.add_error("price",msg)






