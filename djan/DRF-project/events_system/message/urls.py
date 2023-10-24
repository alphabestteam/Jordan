from django.urls import path
from  message.views import MessageCreateView

urlpatterns = [
    path('create-message/', MessageCreateView.as_view(), name='message-create'),
]