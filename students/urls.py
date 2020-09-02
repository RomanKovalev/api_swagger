from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from crud.views import StudentViewSet

schema_view = get_swagger_view(title='Students CRUD')

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', schema_view),
    path(r'api/', include(router.urls)),
]
