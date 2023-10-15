from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from note.views import NoteViewset

schema_view = get_schema_view(
   openapi.Info(
      title="Guest Book API Routes",
      default_version='v1',
      description="Guest Book API's backend public endpoints to call from React JS frontend",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('', NoteViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
