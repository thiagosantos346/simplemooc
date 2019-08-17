from django.test import TestCase

from course.models import CourseManager

class CourseManagerTestCase(TestCase):
	def setUp(self):
		CourseManager.search("")