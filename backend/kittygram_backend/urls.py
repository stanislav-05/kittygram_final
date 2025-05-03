from cats.views import AchievementViewSet, CatViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

API_PREFIX = 'api/'

api_patterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),  # Работа с пользователями
    path('', include('djoser.urls.authtoken')),  # Работа с токенами
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX, include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
