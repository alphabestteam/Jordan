from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllPeople', views.get_all_people),
    path('api/addPerson', views.add_person),
    path('api/removePerson/<str:id_number>', views.remove_person),
    path('api/updatePerson', views.update_person),
]
