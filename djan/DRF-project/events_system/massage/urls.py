from django.urls import path, include
from .views import ChatMassageViewSet,ChatViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'massage', ChatMassageViewSet)

urlpatterns = [
    path('massage/', ChatMassageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('chat/', ChatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('massage/<int:sender>/', ChatMassageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]