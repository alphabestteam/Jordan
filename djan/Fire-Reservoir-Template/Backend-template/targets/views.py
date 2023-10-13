from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TargetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=405)  

@csrf_exempt
def update_target(request):
    try:
        target = Target.objects.get(target_id=target_id)
    except Target.DoesNotExist:
        return HttpResponse(status=404) 

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TargetSerializer(target, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=405)

def all_targets(request):
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=405) 
