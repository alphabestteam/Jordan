from django.http import JsonResponse
from django.db.models import Q, Avg, Sum, F, Count
from .models import Parent, Person 
def parents_details(request):
    return JsonResponse(list(Parent.objects.values()), safe=False)

def google_parents(request):
    google_parents_count = Parent.objects.filter(workplace="Google").count()
    return JsonResponse({'google_parents_count': google_parents_count})

def sorted_parents_by_child_birthdate(request):
    sorted_parents = Parent.objects.order_by("-children__birth_date").values()
    return JsonResponse(list(sorted_parents), safe=False)

def people_with_i_in_name(request):
    people_with_i_in_name = Parent.objects.filter(name__icontains='i').values()
    return JsonResponse(list(people_with_i_in_name), safe=False)

def parents_in_raanana_tel_aviv(request):
    parents_in_raanana_tel_aviv = Parent.objects.filter(Q(city="Raanana") | Q(city="Tel Aviv")).values()
    return JsonResponse(list(parents_in_raanana_tel_aviv), safe=False)

def average_salary(request):
    average_salary = Parent.objects.aggregate(avg_salary=Avg('base_salary'))
    return JsonResponse(average_salary, safe=False)

def parents_with_children_count(request):
    parents_with_children_count = Parent.objects.annotate(children_count=Count('children'))
    result = [{'name': parent.name, 'children_count': parent.children_count} for parent in parents_with_children_count]
    return JsonResponse(result, safe=False)


def total_children_count(request):
    parents = Parent.objects.all()
    total_children_count = sum(parent.children.all().count() for parent in parents)
    return JsonResponse({'children_count': total_children_count}, safe=False)


def highest_salary_parent(request):
    highest_salary_parent = Parent.objects.order_by('-base_salary').values('name', 'base_salary').first()
    return JsonResponse(highest_salary_parent, safe=False)

def children_with_high_earning_parents(request):
    children_with_high_earning_parents = Person.objects.filter(parents__base_salary__gte=50000).values()
    return JsonResponse(list(children_with_high_earning_parents), safe=False)