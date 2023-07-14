from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Thurisa Academy API Documentation",
        default_version='v1',
        description=" Coming soon",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@thurisalearn.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/academy/', include('academy.urls', namespace='academy')),
    path('api/v1/blog/', include('blog.urls', namespace='blog')),
    path('api/v1/work/', include('work.urls', namespace='work')),

    # Documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Thurisa Academy Control Panel'
admin.site.index_title = 'Administrators Dashboard'
admin.site.site_title = 'Control Panel'
