from django.views.generic import ListView, DetailView
from .models import Client, Credit, Account


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'
    pk_url_kwarg = 'client_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = self.object.account_set.all()
        context['credits'] = Credit.objects.filter(account__client=self.object)
        return context
