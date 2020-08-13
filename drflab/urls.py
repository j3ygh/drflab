from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'))),
    path('api/', include(('rest_framework.urls', 'rest_framework'))),
    path('usage/', include(('usage.urls', 'usage'))),
    path('', RedirectView.as_view(url='/api/'), name='index')
]
