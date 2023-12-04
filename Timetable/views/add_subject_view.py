from django.shortcuts import render, redirect
from ..forms import SubjectForm
from ..models import Subject
from django.http import JsonResponse
import aspectlib
import json


@aspectlib.Aspect
def log_add_subject(*args, **kwargs):
    print("Adding a subject...")
    result = yield aspectlib.Proceed
    print("Subject added successfully.")
    return result


@aspectlib.Aspect
def log_update_subject(*args, **kwargs):
    print("Update a subject...")
    result = yield aspectlib.Proceed
    print("Subject updated successfully.")
    return result


@aspectlib.Aspect
def log_delete_subject(*args, **kwargs):
    print("Delete a subject...")
    result = yield aspectlib.Proceed
    print("Subject deleted successfully.")
    return result


@aspectlib.Aspect
def log_get_students(*args, **kwargs):
    print("Get subjects...")
    result = yield aspectlib.Proceed
    print("Subjects received successfully.")
    return result


@log_add_subject
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = Subject(
                name=form.cleaned_data['name']
            )
            subject.save()
            return redirect('index')  

    else:
        form = SubjectForm()

    return render(request, 'index.html', {'form': form})


@log_update_subject
def update_subject(request, subject_id):
    try:
        if request.method == 'PUT':
            print(f"Processing PUT request for student ID {subject_id}")
        else:
            print(f"Invalid request method")
        
        subject = Subject.objects.get(id=subject_id)
        data = json.loads(request.body)

        subject.name = data.get('name', subject.name)

        subject.save()  

        updated_data = {
                'name': subject.name,
                
            }
        
        print(updated_data)
        return JsonResponse(updated_data)

    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@log_delete_subject
def delete_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        subject.delete()
        
        return JsonResponse({'message': 'Student deleted successfully'})
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@log_get_students
def get_all_subjects(request):
    subjects = Subject.objects.all()
    subjects_data = []
    for subject in subjects:
        subject_data = {
            'name': subject.name,
            
        }
        subjects_data.append(subject_data)
    return JsonResponse(subjects_data, safe=False)