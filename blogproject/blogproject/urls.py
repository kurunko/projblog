from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('noticias/', include('topics.urls', namespace='threads')),
    re_path(r'^chaining/', include('smart_selects.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)