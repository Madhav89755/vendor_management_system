"""
URL configuration for vendor_mgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView)

urlpatterns = [
    path("generate/", TokenObtainPairView.as_view(),
         name="generate-jwt-token"),
    path("refresh/", TokenRefreshView.as_view(), name="jwt-refresh-token"),
    path("verify/", TokenVerifyView.as_view(), name="jwt-verify-refresh"),
    path("admin/", admin.site.urls),
    path("", include("vendor.urls"))
]
