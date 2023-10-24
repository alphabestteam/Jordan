from django.urls import path
from .views import FileCreateView

urlpatterns = [
    path('create-file/', FileCreateView.as_view(), name='file-create'),
]