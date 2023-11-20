from django.shortcuts import render, redirect
from ..forms import StudentForm
from ..models import Student


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Create a Student instance using the form data
            student = Student(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            student.save()
            return redirect('index')  # Redirect to the index page after successful submission
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})
