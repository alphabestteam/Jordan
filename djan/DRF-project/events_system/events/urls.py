
from django.urls import path
from .views import BasicFormList,BasicFormDetail,basic_form_list,add_user_to_shared_users

urlpatterns = [
    path('basic_forms/', BasicFormList.as_view(), name='basicform-list'),
    path('basic_forms/<int:pk>/', BasicFormDetail.as_view(), name='basicform-detail'),
    path('basic_forms/list/', basic_form_list, name='basicform-list-api'),
    path('basic_forms/<int:form_id>/add_user/<int:user_id>/', add_user_to_shared_users, name='add-user-to-shared-users'),
]
