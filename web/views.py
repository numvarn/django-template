from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import datetime
from .models import Student
from .forms import StudentForm


# 1. READ: List all students (Home page)
def index(request):
    students = Student.objects.all().select_related("major")
    context = {
        "title": "รายชื่อนักศึกษา (Student List)",
        "students": students,
        "date": datetime.date.today(),
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# 2. READ: Student detail view
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        "title": "ข้อมูลนักศึกษา (Student Detail)",
        "student": student,
    }
    return render(request, "student_detail.html", context)


# 3. CREATE: Add new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(
                request,
                f"เพิ่มข้อมูลนักศึกษา '{student.prefix_name}{student.fname} {student.lname}' เรียบร้อยแล้ว",
            )
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm()

    context = {
        "title": "เพิ่มข้อมูลนักศึกษา (Add Student)",
        "form": form,
    }
    return render(request, "student_form.html", context)


# 4. UPDATE: Edit existing student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"แก้ไขข้อมูลนักศึกษา '{student.prefix_name}{student.fname} {student.lname}' เรียบร้อยแล้ว",
            )
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)

    context = {
        "title": "แก้ไขข้อมูลนักศึกษา (Edit Student)",
        "form": form,
        "student": student,
    }
    return render(request, "student_form.html", context)


# 5. DELETE: Delete student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student_name = f"{student.prefix_name}{student.fname} {student.lname}"
        student.delete()
        messages.success(request, f"ลบข้อมูลนักศึกษา '{student_name}' เรียบร้อยแล้ว")
        return redirect("home")

    context = {
        "title": "ยืนยันการลบข้อมูล (Delete Student)",
        "student": student,
    }
    return render(request, "student_confirm_delete.html", context)
