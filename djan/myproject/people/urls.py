from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllPeople', views.get_all_people),
    path('api/addPerson', views.add_person),
    path('api/removePerson/<str:id_number>', views.remove_person),
    path('api/updatePerson', views.update_person),
    path('api/createParents', views.create_or_list_parents),
    path('api/linkChild', views.link_child_to_parent),
    path('api/retrieveParent/<int:parent_id>', views.retrieve_parent_with_children),
    path('api/richChildren', views.rich_children),
    path('api/findParents/<int:person_id>', views.find_parents),
    path('api/retrieveChildren', views.retrieve_children_of_parent),
    path('api/findGrandparents/<int:person_id>', views.find_grandparents),
    path('api/findSiblings/<int:person_id>', views.find_siblings),
]
