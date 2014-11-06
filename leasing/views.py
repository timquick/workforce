from leasing.forms import StaffForm
from leasing.models import Staff  
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy


class ListStaff(ListView):
    template_name = 'leasing/staff_list.html'
    model = Staff
    def get_context_data(self, **kwargs):
        context = super(ListStaff, self).get_context_data(**kwargs)
        context['object_name'] = 'Staff'
        return context

class ViewStaff(DetailView):
    model = Staff
    template_name = 'leasing/staff_detail.html'

class EditStaff(UpdateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy('leasing:staff_list')
    template_name = 'leasing/staff_form.html'
        
class NewStaff(CreateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy('staff_list')
    template_name = 'leasing/staff_form.html'
        


