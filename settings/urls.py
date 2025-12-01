# Django modules
from django.contrib import admin
from django.urls import path,include

# Project modules
from apps.tasks.views import hello_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route="hello/", view=hello_view, name="hello-view"),
    path('api/education/',include('apps.education.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
