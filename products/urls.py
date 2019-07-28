from django.conf.urls import url

from .views import get_stores,success,add_new_stores,home,StoreView,\
    ProductsView,AddProductsView

urlpatterns = [

    url(r'home/',home),
    url(r'get_stores/',get_stores,name = 'store_details'),
    url(r'success/',success,name='success'),
    url(r'add_stores/',add_new_stores,name = 'add_store'),

    url(r'get_products/',ProductsView.as_view(),name='prod_details'),
    url(r'add_produts/',AddProductsView.as_view(),name = 'add_prods'),


    url(r'store_data/',StoreView.as_view())

]