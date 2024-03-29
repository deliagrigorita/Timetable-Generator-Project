from django.shortcuts import render, redirect
from ..forms import AdminForm 
from ..models import Admin, User
from django.http import JsonResponse
import aspectlib
import json
from django.shortcuts import get_object_or_404

@aspectlib.Aspect
def log_add_admin(*args, **kwargs):
    print("Adding a admin...")
    result = yield aspectlib.Proceed
    print("Admin added successfully.")
    return result

@aspectlib.Aspect
def log_update_admin(*args, **kwargs):
    print("Update a admin...")
    result = yield aspectlib.Proceed
    print("Admin updated successfully.")
    return result

@aspectlib.Aspect
def log_delete_admin(*args, **kwargs):
    print("Delete a admin...")
    result = yield aspectlib.Proceed
    print("Admin deleted successfully.")
    return result

@aspectlib.Aspect
def log_get_admins(*args, **kwargs):
    print("Get admins...")
    result = yield aspectlib.Proceed
    print("Admins received successfully.")
    return result

def add_admin(request):
    users = User.objects.all()  
    form = AdminForm(initial={'user': User.objects.all().first()})
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']

            admin_instance = form.save(commit=False)

            admin_instance.user = user

            admin_instance.save()

            return redirect('index')  
    else:
        form = AdminForm()

    return render(request, 'admin.html', {'users': users, 'form': form})
       


@log_update_admin
def update_admin(request, admin_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for admin ID {admin_id}")
        else:
            print(f"Invalid request method")
        
        admin = Admin.objects.get(id=admin_id)
        data = json.loads(request.body)


        admin.save()

        updated_data = {
            
        }

        return JsonResponse(updated_data)

    except Admin.DoesNotExist:
        return JsonResponse({'error': 'Admin not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_delete_admin
def delete_admin(request, admin_id):
    try:
        admin = Admin.objects.get(id=admin_id)
        admin.delete()
        
        return JsonResponse({'message': 'Admin deleted successfully'})
    except Admin.DoesNotExist:
        return JsonResponse({'error': 'Admin not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@log_get_admins
def get_all_admins(request):
    admins = Admin.objects.all()
    admins_data = []
    for admin in admins:
        admin_data = {
            
        }
        admins_data.append(admin_data)
    return JsonResponse(admins_data, safe=False)
