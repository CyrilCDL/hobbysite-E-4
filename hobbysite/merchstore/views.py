from .models import Product, ProductType
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from .models import ProductType, Product, Transaction
from .forms import TransactionForm
from django.views.generic.edit import FormMixin, CreateView, UpdateView
from user_management.models import Profile


class ProductListView(ListView):
    model = ProductType
    template_name = 'items_list.html'


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'items_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'items_create.html'
    fields = ('name', 'product_type', 'description',
              'price', 'stock', 'status')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'items_update.html'
    fields = ('name', 'product_type', 'description',
              'price', 'stock', 'status')
    success_url = reverse_lazy('merchstore:product_type')

    def form_valid(self, form):
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = 'OUT_OF_STOCK'
        else:
            product.status = 'AVAILABLE'
        product.save()
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'items_cart.html'
    context_object_name = 'owner_transactions'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner_transactions = {}
        for transaction in context['owner_transactions']:
            owner = transaction.product.owner
            if owner:
                owner_display_name = owner.display_name
                if owner_display_name not in owner_transactions:
                    owner_transactions[owner_display_name] = []
                owner_transactions[owner_display_name].append(transaction)
        context['owner_transactions'] = owner_transactions
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'items_transaction.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_dict = {}
        for transaction in context['transactions']:
            buyer = transaction.buyer
            if buyer not in transaction_dict:
                transaction_dict[buyer] = []
            transaction_dict[buyer].append(transaction)
        context['transaction_dict'] = transaction_dict
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return reverse('merchstore:cart')
        else:
            return self.render_to_response(self.get_context_data(form=form))
