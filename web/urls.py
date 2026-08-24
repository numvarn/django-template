from django.urls import path
from . import views

urlpatterns = [
    # List (Read)
    path("", views.index, name="home"),
    # Create
    path("student/create/", views.student_create, name="student_create"),
    # Detail (Read)
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    # Update
    path("student/<int:pk>/update/", views.student_update, name="student_update"),
    # Delete
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),
    # Static pages
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
