from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นางสาว", "นางสาว"),
    ("นาง", "นาง"),
)


class Student(models.Model):

    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_id", "prefix_name", "fname", "lname")


# register model
admin.site.register(Student, StudentAdmin)
