from django.forms import ModelForm
from leasing.models import Staff

class StaffForm(ModelForm):
    class Meta():
        model = Staff
        fields = ['name', 'role', 'phone','email']


    
