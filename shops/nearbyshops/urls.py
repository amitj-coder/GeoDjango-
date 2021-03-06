from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("test-data/", views.test_data, name='test_data'),
    # path("city-create/", views.CityCreateView.as_view(), name="create"),
    # path("shop/", views.shop_view, name="shop"),
    # path("distance/", views.distance),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
