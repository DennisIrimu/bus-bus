from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

urlpatterns = [
  url('^$', views.home, name = 'home'),
  url(r'^search/',views.search_results, name = 'search_results'),
  url(r'^bus-details/(\d+)',views.bus_details, name = 'bus_details'),
  url(r'^mobile_payment/(\d+)',views.mobile_payment, name = 'mobile_payment'),
  

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
