from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User


class UserRegistrationTest(TestCase):

    def setUp(self):
        self.register_url = reverse('register')

    def test_registration_page_renders_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_user_can_register_successfully(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_registration_fails_for_duplicate_username(self):
        User.objects.create_user(username='testuser', password='password123', email='testuser@example.com')

        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'newemail@example.com',
            'password': 'newpassword123',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username is already taken')
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)

    def test_registration_fails_for_invalid_data(self):
        response = self.client.post(self.register_url, {
            'username': '',
            'email': 'invalidemail',
            'password': 'short',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required')
        self.assertFalse(User.objects.filter(email='invalidemail').exists())
