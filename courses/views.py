from .forms import AddCourseForm
from django.shortcuts import render, redirect
from .models import Courses


# Create your views here.

def view_courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses/view_courses.html', {'courses': courses})

def add_courses(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)

        if form.is_valid():
            courses = form.save()
            courses.save()

            return redirect('add_courses')
    else:
        form = AddCourseForm()
    
    return render(request, 'courses/add_courses.html', {'form': form})

def update_course(request, course_id):
    course = Courses.objects.get(pk=course_id)
    
    if request.method == 'POST':
        form = AddCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_courses')
    else:
        form = AddCourseForm(instance=course)

    return render(request, 'courses/update_course.html', {'form': form, 'course': course})

def course_detail(request, course_id):
    courses = Courses.objects.get(pk=course_id)

    return render(request, 'courses/course_detail.html', {'courses': courses})

def delete_course(request, course_id):
	courses = Courses.objects.get(pk=course_id)

	if request.method == 'POST':
		courses.delete()

		return redirect('view_courses')

	return render(request, 'courses/delete_course.html', {'courses': courses})