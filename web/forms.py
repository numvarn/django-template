from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["st_id", "prefix_name", "fname", "lname", "major"]
        labels = {
            "st_id": "รหัสนักศึกษา (Student ID)",
            "prefix_name": "คำนำหน้าชื่อ (Prefix)",
            "fname": "ชื่อ (First Name)",
            "lname": "นามสกุล (Last Name)",
            "major": "สาขาวิชา (Major)",
        }
        widgets = {
            "st_id": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "เช่น 650123456789"}
            ),
            "prefix_name": forms.Select(attrs={"class": "form-select"}),
            "fname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "กรอกชื่อจริง"}
            ),
            "lname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "กรอกนามสกุล"}
            ),
            "major": forms.Select(attrs={"class": "form-select"}),
        }
