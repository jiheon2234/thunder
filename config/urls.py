from django.contrib import admin
from django.urls import path, include
from goods import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexLV.as_view(), name='index'),
    path('goods/', include('goods.urls')),
    path('common/', include('common.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)