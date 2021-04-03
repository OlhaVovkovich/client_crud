from django.urls import reverse_lazy
from django.forms.widgets import SelectDateWidget
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client


client_fields = ['first_name', 'last_name', 'address', 'date_of_birth']


class ClientList(ListView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    fields = client_fields
    success_url = reverse_lazy('client-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'create'
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = SelectDateWidget(
            years=list(range(1960, 2022)),
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
        return form


class ClientUpdate(UpdateView):
    model = Client
    fields = client_fields
    success_url = reverse_lazy('client-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'update'
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = SelectDateWidget(
            years=list(range(1960, 2022)),
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
        return form


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')
