from django.conf.urls import url
from .views import cart_add,cart_remove,cart_detail,checkout
urlpatterns = [
    url(r'^$',cart_detail, name='cart_detail'),
    url(r'^add/photos/(?P<id>\d+)/$',
         cart_add,
        name='cart_add'),
    url(r'^remove(?P<id>\d+)/$',
        cart_remove,
        name='cart_remove'),
    url(r'^checkout/$',checkout,name='checkout')
    
]