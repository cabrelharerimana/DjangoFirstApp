from django.shortcuts import redirect, render, get_object_or_404

from .models import *
from.forms import studentForm
from .models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, id):
    student_instance = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html', {'student': student_instance})

def student_create(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
            form = studentForm()

    return render(request, 'students/student_form.html', {'form':form})
    

def student_update(request, id):
        student_instance = get_object_or_404(Student, id=id)
        if request.method == 'POST':
            form = studentForm(request.POST, instance=student_instance)
            if form.is_valid():
              form.save()
            return redirect('student_list')
        else:
                form = studentForm(instance=student_instance)
                return render(request, 'students/student_form.html', {'form':form})
            
def student_delete(request, id):
        student_instance = get_object_or_404(Student, id=id)
        if request.method == 'POST':
            student_instance.delete()
            return redirect('student_list')
        return render(request, 'students/student_delete.html', {'student':student_instance})
            

