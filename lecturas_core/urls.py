from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('coleccion.urls')),  # <- Esto incluye tus endpoints
    path('api/usuarios/', include('usuarios.urls')),  # <- si ya creaste login/registro 
    path('estadisticas/', include('estadisticas.urls')),
]

# Archivos media (PDFs)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
