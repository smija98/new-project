from django.test import TestCase

# Create your tests here.
def demo(txt1,txt2):
    return txt1+txt2

class Testdemo(TestCase):
    def test_concatenate(self):
        self.assertEqual(demo("python"," program"),"python program")