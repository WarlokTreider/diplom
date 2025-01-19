"""netology_pd_diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from baton.autodiscover import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/v1/', include('backend.urls', namespace='backend')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('oauth/', include('social_django.urls', namespace='social')),

    # path('social/', include('social.apps.django_app.urls', namespace='social')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('accounts/', include('allauth.urls')),


]