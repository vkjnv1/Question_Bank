from django.forms import ModelForm
from .models import add

class UpdateForm(ModelForm):
    class Meta:
        model = add
        fields = '__all__'