from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from .serializers import PersonSerializer
import json

@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        people = Person.objects.all().values()  
        return HttpResponse(list(people), safe=False, status=200)
        return HttpResponse({"message": "Invalid request method"}, status=400)


@csrf_exempt    
def add_person(request):
    if request.method == "POST":
        data = json.loads(request.body)
        person = Person(
            id_number=data["id_number"],
            name=data["name"],
            birth_date=data["birth_date"],
            city=data["city"],
        )
        person.save()
        return HttpResponse({"message": "Person added successfully"}, status=200)
    else:
        return HttpResponse({"message": "Invalid request method"}, status=400)

@csrf_exempt      
def remove_person(request, id_number):
    if request.method == "DELETE":
        try:
            person = Person.objects.get(id_number=id_number)
            person.delete()
            return HttpResponse({"message": "Person deleted successfully"}, status=200)
        except Person.DoesNotExist:
            raise Http404("Person does not exist in the database")
    else:
        return HttpResponse({"message": "Invalid request method"}, status=400)

@csrf_exempt
def update_person(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            person = Person.objects.get(id_number=data["id_number"])
            person.name = data["name"]
            person.birth_date = data["birth_date"]
            person.city = data["city"]
            person.save()
            return HttpResponse({"message": "Person updated successfully"}, status=200)
        except Person.DoesNotExist:
            return HttpResponse({"message": "Person not found"}, status=404)
    else:
        return HttpResponse({"message": "Invalid request method"}, status=400)

