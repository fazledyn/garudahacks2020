from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'donors',      views.DonorViewSet,         basename='donor')
router.register(r'newsletters', views.NewsletterViewSet,    basename='newsletter')
router.register(r'users',       views.UserViewSet,          basename='user')
router.register(r'contacts',    views.ContactViewSet,       basename='contact')

urlpatterns = router.urls