from leasing.forms import StaffForm
from leasing.models import Staff  
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy


class ListStaff(ListView):
    model = Staff

class ViewStaff(DetailView):
    model = Staff
    
class EditStaff(UpdateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy('staff_list')
        
class NewStaff(CreateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy('staff_list')
        


