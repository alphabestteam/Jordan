
from django.urls import path
from .views import BasicFormViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'events', BasicFormViewSet)

urlpatterns = [
    path('basic_form/', BasicFormViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('basic_forms/<int:pk>/', BasicFormViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
 
]

