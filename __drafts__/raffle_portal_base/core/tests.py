from django.test import TestCase
from unittest.result import failfast

# Create your tests here.
class Tests(TestCase):
    def test_dummy(self):
        a = 1+1
        b = 2
        self.assertEquals(a, b)
