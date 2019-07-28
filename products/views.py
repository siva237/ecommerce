from django.shortcuts import render,reverse,redirect
from .models import Stores,Products
from .forms import StoresForm,ProductsForm
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
# Create your views here.


def home(request):
    return render(request,'base.html')


def get_stores(request):

    data = Stores.objects.all()

    return render(request,'store_details.html',{'store_data':data})

def add_new_stores(request):
    if request.method == 'POST':
        form = StoresForm(request.POST)
        if form.is_valid():
            obj = Stores()
            obj.name = form.cleaned_data['name']
            obj.address = form.cleaned_data['address']
            obj.landmark = form.cleaned_data['landmark']
            obj.email = form.cleaned_data['email']
            obj.location = form.cleaned_data['location']
            obj.contact_no = form.cleaned_data['contact_no']
            obj.save()
        else:
            raise form.ValidationErrors
        return HttpResponseRedirect(reverse('success'))
    else:
        form = StoresForm()

    return render(request, 'add_details.html', {'form': form})

def success(request):
    return render(request,'success.html')


class StoreView(ListView):

    model = Stores
    queryset = Stores.objects.all()
    template_name = 'store_details.html'
    context_object_name = 'store_data'


class ProductsView(ListView):

    model = Products
    query_set = Products.objects.all()
    template_name = 'products_details.html'
    context_object_name = 'products_data'


class AddProductsView(FormView):

    template_name = 'add_products.html'
    form_class = ProductsForm
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        # return redirect(self.success_url)
        return HttpResponseRedirect(self.get_success_url())





