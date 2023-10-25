from django.urls import path, include
from .views import UserProfileViewSet, add_unread_message_to_user, mark_message_as_read
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('add_unread_message/<int:id_number>/<int:message_id>/',add_unread_message_to_user, name='add_unread_message_to_user'),
    path('mark_message_as_read/<int:id_number>/<int:message_id>/', mark_message_as_read, name='mark_message_as_read'),
]