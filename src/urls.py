from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from onshop.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onshop.urls')),
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
