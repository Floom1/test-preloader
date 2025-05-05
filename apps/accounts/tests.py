from django.test import TestCase
from django.urls import reverse

class AccountsTests(TestCase):
    def test_signup_page(self):
        """Проверяет, что страница регистрации доступна."""
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign Up")
    def test_login_page(self):
        """Проверяет, что страница входа доступна."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")