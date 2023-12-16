from django.shortcuts import render, redirect
from ..forms import ResourceForm  
from ..models import Resource, Classroom
from django.http import JsonResponse, HttpResponse
import aspectlib
import json
from Timetable.security_aspect import secure_resource_access
from django.http import JsonResponse
import aspectlib
import json

@aspectlib.Aspect
def log_add_resource(*args, **kwargs):
    print("Adding a resource...")
    result = yield aspectlib.Proceed
    print("Resource added successfully.")
    return result

@aspectlib.Aspect
def log_update_resource(*args, **kwargs):
    print("Update a resource...")
    result = yield aspectlib.Proceed
    print("Resource updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_resource(*args, **kwargs):
    print("Delete a resource...")
    result = yield aspectlib.Proceed
    print("Resource deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_resources(*args, **kwargs):
    print("Get resources...")
    result = yield aspectlib.Proceed
    print("Resources received successfully.")
    return result

@secure_resource_access
@log_add_resource
def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)  
        if form.is_valid():
            resource = form.save()
            return redirect('index')  
    else:
        form = ResourceForm()  
    return render(request, 'index.html', {'form': form})

@log_update_resource
def update_resource(request, resource_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for resource ID {resource_id}")
        else:
            print(f"Invalid request method")
        
        resource = Resource.objects.get(id=resource_id)
        data = json.loads(request.body)

        resource.name = data.get('name', resource.name)
        resource.description = data.get('description', resource.description)
        resource.availability = data.get('availability', resource.availability)

        resource.save()

        updated_data = {
            'id': resource.id,
            'name': resource.name,
            'description': resource.description,
            'availability': resource.availability,
        }

        return JsonResponse(updated_data)

    except Resource.DoesNotExist:
        return JsonResponse({'error': 'Resource not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_resource
def delete_resource(request, resource_id):
    try:
        resource = Resource.objects.get(id=resource_id)
        resource.delete()
        
        return JsonResponse({'message': 'Resource deleted successfully'})
    except Resource.DoesNotExist:
        return JsonResponse({'error': 'Resource not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_resources
def get_all_resources(request):
    resources = Resource.objects.all()
    resources_data = []
    for resource in resources:
        resource_data = {
            'id': resource.id,
            'name': resource.name,
            'description': resource.description,
            'availability': resource.availability,
        }
        resources_data.append(resource_data)
    return JsonResponse(resources_data, safe=False)
