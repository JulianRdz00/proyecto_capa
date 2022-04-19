import imp
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfiles.urls')),
    path('', include('django.contrib.auth.urls')),
    path('cursos/', include('cursos.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)