from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:place_id>/', include('tinymce.urls')),
    path('places/<int:place_id>/', views.places, name='place-archive')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
