from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Registration
from .forms import StudentForm, CourseForm, RegistrationForm 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

# Course List (READ)
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Add Course (CREATE)
@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

# Edit Course (UPDATE)
@login_required
def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

# Delete Course (DELETE)
@login_required
def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')



# Registration List
@login_required
def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})

# Add Registration
@login_required
def registration_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

# Edit Registration
@login_required
def registration_update(request, id):
    registration = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'registration_form.html', {'form': form})

# Delete Registration
@login_required
def registration_delete(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.delete()
    return redirect('registration_list')

