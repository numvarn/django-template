from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["st_id", "prefix_name", "fname", "lname", "major"]
        labels = {
            "st_id": "รหัสนักศึกษา",
            "prefix_name": "คำนำหน้าชื่อ",
            "fname": "ชื่อ",
            "lname": "นามสกุล",
            "major": "สาขาวิชา",
        }
        widgets = {
            "st_id": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "เช่น 650123456789",
                }
            ),
            "prefix_name": forms.Select(
                attrs={"class": "form-control form-control-lg form-select"}
            ),
            "fname": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกชื่อจริง",
                }
            ),
            "lname": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกนามสกุล",
                }
            ),
            "major": forms.Select(
                attrs={"class": "form-control form-control-lg form-select"}
            ),
        }
