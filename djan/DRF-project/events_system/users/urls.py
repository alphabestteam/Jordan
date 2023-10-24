from django.urls import path, include
from .views import user_list, UserProfileViewSet
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('api/users/', user_list, name='user-list-api'),
]