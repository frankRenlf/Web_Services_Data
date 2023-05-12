import datetime

from django.test import TestCase

from app01.models import Passenger, payment_method, Order, Flight, Admin
from django.utils import timezone


# Create your tests here.
class MyModelTest1(TestCase):

    def setUp(self):
        Passenger.objects.create(name='Test Model')

    def test_model_name(self):
        test_model = Passenger.objects.get(name='Test Model')
        self.assertEqual(test_model.name, 'Test Model')


class MyModelTest2(TestCase):

    def setUp(self):
        payment_method.objects.create(payment_platform='visa')

    def test_model_name(self):
        test_model = payment_method.objects.get(payment_platform='visa')
        self.assertEqual(test_model.payment_platform, 'visa')


class MyModelTest3(TestCase):

    def setUp(self):
        Flight.objects.create(flight_id=21,
                              airline_name="china",
                              departure_time=timezone.make_aware(datetime.datetime(2023, 5, 3, 14, 30)),
                              arrival_time=timezone.make_aware(datetime.datetime(2023, 5, 4, 17, 30)),
                              departure_location="hz",
                              arrival_location="cd",
                              flight_price=99.3,
                              seat_number=77)

    def test_model_name(self):
        test_model = Flight.objects.get(flight_id=21)
        self.assertEqual(test_model.flight_id, 21)


class MyModelTest5(TestCase):

    def setUp(self):
        Admin.objects.create(name="gzhao", password="123")

    def test_model_name(self):
        test_model = Admin.objects.get(name="gzhao")
        self.assertEqual(test_model.password, "123")


class SimpleTest1(TestCase):
    def test1(self):
        response = self.client.get('/depart/list')
        self.assertEqual(response.status_code, 200)


class SimpleTest2(TestCase):
    def test1(self):
        response = self.client.get('/order_data/')
        self.assertEqual(response.status_code, 200)


class SimpleTest3(TestCase):
    def test1(self):
        response = self.client.get('/flight_data/')
        self.assertEqual(response.status_code, 200)


class SimpleTest4(TestCase):
    def test1(self):
        response = self.client.get('/user/list')
        self.assertEqual(response.status_code, 200)


class SimpleTest5(TestCase):
    def test1(self):
        response = self.client.get('/pretty/list')
        self.assertEqual(response.status_code, 200)


class SimpleTest6(TestCase):
    def test1(self):
        response = self.client.get('/admin/list')
        self.assertEqual(response.status_code, 200)


class SimpleTest7(TestCase):
    def test1(self):
        response = self.client.get('/chart/list')
        self.assertEqual(response.status_code, 200)


class SimpleTest8(TestCase):
    def test1(self):
        response = self.client.get('/upload/list')
        self.assertEqual(response.status_code, 200)
