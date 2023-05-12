from django.test import TestCase
from app01.models import payment_method


class MyModelTest2(TestCase):

    def setUp(self):
        payment_method.objects.create(name='visa')

    def test_model_name(self):
        test_model = payment_method.objects.get(name='visa')
        self.assertEqual(test_model.name, 'visa')
