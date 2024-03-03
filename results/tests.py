from django.test import TestCase
from .models import Student, Unit, Result
from django.contrib.auth.models import User
from datetime import date
# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='####')
        
        # Create a test student
        self.student = Student.objects.create(user=self.user, reg_number='0335', name='kev', course='MCS', year_of_study='1st year', Session='2023/2024')
        
        # Create a test unit
        self.unit = Unit.objects.create(name='Test Unit', unit_code='SMA2101', unit_lecturer='Lec')

        # Create test result
        self.result = Result.objects.create(student=self.student, unit=self.unit, marks=64, exam_type='Supplementary', exam_date=date(2024, 3, 15))

    def test_student_creation(self):
        self.assertEqual(self.student.user.username, 'testuser')
        self.assertEqual(self.student.reg_number, '0335')
        self.assertEqual(self.student.name, 'kev')
        self.assertEqual(self.student.course, 'MCS')
        self.assertEqual(self.student.year_of_study, '1st year')
        self.assertEqual(self.student.Session, '1st Semester 2023/2024')

    def test_unit_creation(self):
        self.assertEqual(self.unit.name, 'Test Unit')
        self.assertEqual(self.unit.unit_code, 'SMA2101')
        self.assertEqual(self.unit.unit_lecturer, 'Lec')

    def test_result_creation(self):
        self.assertEqual(self.result.student, self.student)
        self.assertEqual(self.result.unit, self.unit)
        self.assertEqual(self.result.marks, 64)
        self.assertEqual(self.result.exam_type, 'Supplementary')
        self.assertEqual(self.result.exam_date, date(2024, 3, 15))

