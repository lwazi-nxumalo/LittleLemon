from django.test import TestCase


class PageViewTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get("/restaurant/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_page_loads(self):
        response = self.client.get("/restaurant/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_menu_page_loads(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    def test_bookings_page_loads(self):
        response = self.client.get("/restaurant/reservations/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")


class HealthCheckTest(TestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get("/restaurant/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})