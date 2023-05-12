from django.test import TestCase
from app01.models import Passenger


class MyModelTest1(TestCase):

    def setUp(self):
        Passenger.objects.create(name='Test Model')

    def test_model_name(self):
        test_model = Passenger.objects.get(name='Test Model')
        self.assertEqual(test_model.name, 'Test Model')
