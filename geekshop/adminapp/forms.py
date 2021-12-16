from django import forms
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from mainapp.models import ProductCategory



class ShopUserAdminForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(ProductCategoryEditForm).__init__(*args, **kwargs)
            for field.name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''



