from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter



schema_view = get_schema_view(
   openapi.Info(
      title="Food Delivery API",
      default_version='v1',
      description="This is a REST API for a Food Delivery service",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mujahid30390@gmail.com"),
      license=openapi.License(name="Mujahid License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentic.urls')),
    #path('',include('orders.urls')),

    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('auth/', include('djoser.urls.jwt')),
]
