from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  EventViewSet,RSVPViewSet,InvitaionViewSet,EventInfoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'event', EventViewSet)
router.register(r'rsvp', RSVPViewSet)
router.register(r'invitation', InvitaionViewSet)
router.register(r'event-info', EventInfoViewSet)

urlpatterns = [
    path('', include(router.urls))
    
]
