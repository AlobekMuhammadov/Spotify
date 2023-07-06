from asosiy.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("albomlar",AlbomModelViewSet)
router.register("artistlar",ArtistModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist/<int:pk>/', ArtistDetail.as_view()),
    # path('artistlar/', ArtistlarAPIView.as_view()),
    path('', include(router.urls)),
]
