from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'signup', CustomUserViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
