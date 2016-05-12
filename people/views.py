from django.shortcuts import render
from django.views.generic.list import ListView
from people.models import Category, Person
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from people.forms import CategoryForm, PersonForm
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

class CategoryMixin(object):
    model = Category
    #def get_context_data(self, **kwargs):
    #    kwargs.update({'object_name':'Category'})
    #    return kwargs

class CategoryFormMixin(CategoryMixin):
    form_class = CategoryForm

class CategoryList(ListView):
    model = Category
        
class NewCategory(CategoryFormMixin, CreateView):
    pass

class EditCategory(CategoryFormMixin, UpdateView):
    pass

class ViewCategory(CategoryFormMixin, DetailView):
    pass

class DeleteCategory(CategoryMixin, DeleteView):
    template_name = 'people/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('category_list')

class PersonMixin(object):
    model = Person
    #def get_context_data(self, **kwargs):
    #    kwargs.update({'object_name':'Person'})
    #    return kwargs

class PersonFormMixin(PersonMixin):
    form_class = PersonForm

class PeopleList(ListView):
    model = Person
    
class ViewPerson(PersonFormMixin, DetailView):
    pass

class NewPerson(PersonFormMixin, CreateView):
    pass

class EditPerson(PersonFormMixin, UpdateView):
    pass

class DeletePerson(PersonMixin, DeleteView):
    template_name = 'people/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('people_list')

