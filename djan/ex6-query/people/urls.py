from django.urls import path
from . import views


urlpatterns = [
     path('api/all-parents', views.parents_details),
    path('api/google-parents', views.google_parents),
    path('api/sorted-parents', views.sorted_parents_by_child_birthdate, name='sorted_parents_by_child_birthdate'),
    path('api/people-with-i-in-name', views.people_with_i_in_name, name='people_with_i_in_name'),
    path('api/parents-in-raanana-tel-aviv', views.parents_in_raanana_tel_aviv, name='parents_in_raanana_tel_aviv'),
    path('api/average-salary', views.average_salary, name='average_salary'),
    path('api/parents-with-children-count', views.parents_with_children_count, name='parents_with_children_count'),
    path('api/total-children-count', views.total_children_count, name='total_children_count'),
    path('api/highest-salary-parent', views.highest_salary_parent, name='highest_salary_parent'),
    path('api/children-with-high-earning-parents', views.children_with_high_earning_parents, name='children_with_high_earning_parents'),
]
