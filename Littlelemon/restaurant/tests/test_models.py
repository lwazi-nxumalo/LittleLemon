from django.test import TestCase
from django.db.utils import IntegrityError
from restaurant.models import Booking, Menu


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            first_name="Alice",
            reservation_date="2026-08-01",
            reservation_slot=12,
        )

    def test_str_representation(self):
        self.assertEqual(str(self.booking), "Alice -  2026-08-01")

    def test_unique_together_constraint(self):
        with self.assertRaises(IntegrityError):
            Booking.objects.create(
                first_name="Bob",
                reservation_date="2026-08-01",
                reservation_slot=12,
            )


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Bruschetta",
            price="8.99",
            inventory=50,
        )

    def test_str_representation(self):
        self.assertEqual(str(self.menu_item), "Bruschetta")