from django import forms
from app1.models import Root

class RootForm(forms.ModelForm):
    class Meta:
        model = Root
        fields = '__all__'