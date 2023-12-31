"""bashmemo_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from bookmark.views import BookmarkViewSet, LoginSuccessView, UserDetailView, CreateUserView

router = routers.DefaultRouter()

router.register('bookmarks', BookmarkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('api/users/', CreateUserView.as_view()),
    path('api/users/self/', UserDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/success/', LoginSuccessView.as_view(), name="login_success")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


