from django.forms import ModelForm
from .models import Product,Brand


class BrandCreateFrom(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"

class ProductCreateFrom(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
