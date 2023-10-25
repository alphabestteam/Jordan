from django.urls import path
from .views import FileFormViewSet, add_user_to_shared_users
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'file', FileFormViewSet)

urlpatterns = [
    path('file/', FileFormViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('file/<int:uploader>/', FileFormViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('file/<int:uploader>/add_user/<int:id_number>/', add_user_to_shared_users, name='add-user-to-shared-users'),

]