from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Booking, Menu
from restaurant.serializers import MenuSerializer


class MenuAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.menu_item = Menu.objects.create(title="Pizza", price="12.50", inventory=10)
        self.list_url = "/restaurant/api/menu/"
        self.detail_url = f"/restaurant/api/menu/{self.menu_item.id}/"

    def test_anonymous_can_list_menu(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_can_retrieve_menu_item(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_cannot_create_menu_item(self):
        response = self.client.post(self.list_url, {
            "title": "Pasta", "price": "9.99", "inventory": 5
        })
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_anonymous_cannot_update_menu_item(self):
        response = self.client.put(self.detail_url, {
            "title": "Updated", "price": "9.99", "inventory": 5
        })
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_anonymous_cannot_delete_menu_item(self):
        response = self.client.delete(self.detail_url)
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_authenticated_can_create_menu_item(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url, {
            "title": "Pasta", "price": "9.99", "inventory": 5
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_can_update_menu_item(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.detail_url, {
            "title": "Updated Pizza", "price": "13.50", "inventory": 8
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_can_delete_menu_item(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_matches_serializer_output(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pasta", price=120, inventory=50)
        response = self.client.get(reverse('menu-api'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)


class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.booking = Booking.objects.create(
            first_name="Alice", reservation_date="2026-08-01", reservation_slot=12
        )
        self.list_url = "/restaurant/api/bookings/"
        self.detail_url = f"/restaurant/api/bookings/{self.booking.id}/"

    def test_anonymous_cannot_list_bookings(self):
        response = self.client.get(self.list_url)
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_anonymous_cannot_create_booking(self):
        response = self.client.post(self.list_url, {
            "first_name": "Bob", "reservation_date": "2026-08-02", "reservation_slot": 14
        })
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_authenticated_can_list_bookings(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url, {
            "first_name": "Bob", "reservation_date": "2026-08-02", "reservation_slot": 14
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_duplicate_slot_and_date_rejected(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url, {
            "first_name": "Charlie", "reservation_date": "2026-08-01", "reservation_slot": 12
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_bookings_by_date(self):
        Booking.objects.create(first_name="Dana", reservation_date="2026-08-05", reservation_slot=15)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url, {"date": "2026-08-01"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "Alice")