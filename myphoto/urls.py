from django.conf.urls import url,include
from django.contrib import admin
from photos import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    url(r'^myphoto_root/', admin.site.urls),
    url(r'^photos/', include("photos.urls",namespace="photos")),
    url(r'^$',views.home,name="home"),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^accounts/',include("accesslog.urls",namespace="auth"))
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)