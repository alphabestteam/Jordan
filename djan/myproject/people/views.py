from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.core import serializers
from .models import Person, Parent
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils import timezone
from .serializers import PeopleSerializer, ParentSerializer
from rest_framework import serializers
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta


@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        people = Person.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse({"message": "Invalid request method"}, safe=False, status=400)

@csrf_exempt
def add_person(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Person added successfully", status=200)
        else:
            return HttpResponse(json.dumps(serializer.errors), content_type="application/json", status=400)
    else:
        return HttpResponse("Invalid request method", status=400)

@csrf_exempt
def remove_person(request, id_number):
    if request.method == "DELETE":
        try:
            person = Person.objects.get(id_number=id_number)
            person.delete()
            return HttpResponse("Person deleted successfully", status=200)
        except Person.DoesNotExist:
            raise Http404("Person does not exist in the database")
    else:
        return HttpResponse("Invalid request method", status=400)

@csrf_exempt
def update_person(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            person = Person.objects.get(id_number=data["id_number"])
            serializer = PeopleSerializer(person, data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse("Person updated successfully", status=200)
            else:
                return HttpResponse(json.dumps(serializer.errors), content_type="application/json", status=400)
        except Person.DoesNotExist:
            return HttpResponse("Person not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=400)


@csrf_exempt
def create_or_list_parents(request):
    if request.method == "GET":
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = ParentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Parent added successfully", content_type='text/plain', status=200)
        else:
            return HttpResponse(json.dumps(serializer.errors), content_type='application/json', status=400)
    else:
        return HttpResponse("Invalid request method", content_type='text/plain', status=400)

@csrf_exempt
def link_child_to_parent(request):
    if request.method == "POST":
        data = json.loads(request.body)
        parent_id = data.get('parent_id')
        child_id = data.get('child_id')
        try:
            parent = Parent.objects.get(id_number=parent_id)
            child = Person.objects.get(id_number=child_id)
        except Parent.DoesNotExist:
            return HttpResponse("Parent or Child not found", content_type='text/plain', status=404)
        parent.children.add(child)
        parent.save()
        return HttpResponse("Child linked to Parent successfully", content_type='text/plain', status=200)
    else:
        return HttpResponse("Invalid request method", content_type='text/plain', status=400)

@csrf_exempt
def retrieve_parent_with_children(request, parent_id):
    if request.method == "GET":
        try:
            parent = Parent.objects.get(id_number=parent_id) 
            serializer = ParentSerializer(parent, context={'request': request})
            return JsonResponse(serializer.data, status=200, safe=False)
        except Parent.DoesNotExist:
            return HttpResponse("Parent not found", content_type='text/plain', status=404)
    else:
        return HttpResponse("Invalid request method", content_type='text/plain', status=400)

@csrf_exempt
def rich_children(request):
    if request.method == "GET":
        eighteen_years_ago = datetime.now() - timedelta(days=365*18)
        rich_parents = Parent.objects.filter(base_salary__gte=50000)
        rich_children = Person.objects.filter(Q(birth_date__gte = eighteen_years_ago) & Q(parent__in=rich_parents))
        serializer = ParentSerializer(rich_children, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    else:
        return HttpResponse("Invalid request method", content_type='text/plain', status=400)


class ParentsAPI(APIView):
    def get(self, request, person_id):
        try:
            person = People.objects.get(id_number=person_id)
            parents = person.parents.all()
            serializer = PeopleSerializer(parents, many=True)
            return Response(serializer.data, status=200)
        except People.DoesNotExist:
            return Response("Person not found", status=404)

@csrf_exempt
def find_parents(request, person_id):
    try:
        person = Person.objects.get(id_number= person_id)
        parents = person.parents.all()
        parent_data = [{'id_number': parent.id_number,'name': parent.name,  'birth_date': parent.birth_date, 'city': parent.city} for parent in parents]
        return JsonResponse(parent_data, safe=False, status=200)
    except Person.DoesNotExist:
        return JsonResponse("Person not found", safe=False, status=404)

@csrf_exempt
def retrieve_children_of_parent(request, parent_id):
    try:
        parent = People.objects.get(id_number =parent_id)
        children = parent.children.all()
        child_data = [{'name': child.name, 'id_number': child.id_number, 'birth_date': child.birth_date, 'city': child.city} for child in children]
        return JsonResponse(child_data, safe=False, status=200)
    except People.DoesNotExist:
        return JsonResponse("Parent not found", safe=False, status=404)

@csrf_exempt
def find_grandparents(request, person_id):
    try:
        person = Person.objects.get(id_number=person_id)
        parents = person.parents.all()
        grandparent_names = []
        for parent in parents:
            if parent.children.exclude(id_number=person_id).exists():
                grandparent_names.append(parent.name)
        return JsonResponse(grandparent_names, safe=False, status=200)
    except Person.DoesNotExist:
        return JsonResponse("Person not found", safe=False, status=404)

@csrf_exempt
def find_siblings(request, person_id):
    try:
        person = Person.objects.get(id_number=person_id)
        sibling_names = []
        parents = person.parents.all()
        for parent in parents:
            siblings = parent.children.exclude(id_number=person_id)
            sibling_names.extend([sibling.name for sibling in siblings])
        return JsonResponse(sibling_names, safe=False, status=200)
    except Person.DoesNotExist:
        return JsonResponse("Person not found", safe=False, status=404)