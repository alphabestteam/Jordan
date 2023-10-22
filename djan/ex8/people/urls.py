from django.urls import path
from . import views


urlpatterns = [
    path('api/getAllPeople', views.get_all_people),
    path('api/addPerson', views.add_person),
    path('api/removePerson/<str:id_number>', views.remove_person),
    path('api/updatePerson', views.update_person),
    path('create-or-list-parents/', views.create_or_list_parents, name='create_or_list_parents'),
    path('link-child-to-parent/', views.link_child_to_parent, name='link_child_to_parent'),
    path('retrieve-parent-with-children/<int:parent_id>/', views.retrieve_parent_with_children, name='retrieve_parent_with_children'),
    path('rich-children/', views.rich_children, name='rich_children'),
    path('api/findParents/<int:person_id>', views.find_parents, name='find_parents'),
    path('api/retrieveChildren', views.retrieve_children_of_parent, name='retrieve_children_of_parent' ),
    path('api/findGrandparents/<int:person_id>', views.find_grandparents),
    path('api/findSiblings/<int:person_id>', views.find_siblings),
]