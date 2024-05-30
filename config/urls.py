from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg. views import get_schema_view
from drf_yasg import openapi
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
        openapi.Info(
            title="Cars API",
            default_version="version 1",
            description="Swagger (documentation) for CarsAPI project",
        ),
        public=True,
        permission_classes=[permissions.AllowAny]
    )


urlpatterns = [
    path('admin/', admin.site.urls),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-vi'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-cedoe'),


    path('api/', include('cars.urls')),
    # path('rest-auth/', include('rest_framework.urls'))
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings. MEDIA_ROOT)

