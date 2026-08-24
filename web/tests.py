from django.test import TestCase
from django.urls import reverse
from .models import Student, Major


class StudentCRUDTests(TestCase):
    def setUp(self):
        self.major = Major.objects.create(mj_name="วิทยาการคอมพิวเตอร์")
        self.student = Student.objects.create(
            st_id="650000000001",
            prefix_name="นาย",
            fname="สมชาย",
            lname="ใจดี",
            major=self.major,
        )

    def test_student_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "650000000001")
        self.assertContains(response, "สมชาย")

    def test_student_detail_view(self):
        response = self.client.get(
            reverse("student_detail", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "650000000001")
        self.assertContains(response, "วิทยาการคอมพิวเตอร์")

    def test_student_create_view(self):
        # GET request
        response = self.client.get(reverse("student_create"))
        self.assertEqual(response.status_code, 200)

        # POST request
        response = self.client.post(
            reverse("student_create"),
            {
                "st_id": "650000000002",
                "prefix_name": "นางสาว",
                "fname": "สมหญิง",
                "lname": "รักเรียน",
                "major": self.major.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        new_student = Student.objects.get(st_id="650000000002")
        self.assertEqual(new_student.fname, "สมหญิง")

    def test_student_update_view(self):
        # GET request
        response = self.client.get(
            reverse("student_update", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 200)

        # POST request
        response = self.client.post(
            reverse("student_update", kwargs={"pk": self.student.pk}),
            {
                "st_id": "650000000001",
                "prefix_name": "นาย",
                "fname": "สมชาย (แก้ไข)",
                "lname": "ใจดี",
                "major": self.major.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.fname, "สมชาย (แก้ไข)")

    def test_student_delete_view(self):
        # GET confirmation request
        response = self.client.get(
            reverse("student_delete", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 200)

        # POST delete request
        response = self.client.post(
            reverse("student_delete", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
