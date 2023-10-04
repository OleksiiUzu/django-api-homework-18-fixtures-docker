from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class FirstTest(TestCase):
    fixtures = ['all_data.json']

    def test_user_login(self):
        user_client = Client()
        response = user_client.post('/user/login', {'username': 'somName', 'password': 'somePassword'})
        status_code = response.status_code
        self.assertEqual(status_code, 404)

        response = user_client.post('/user/login', {"username": "ggg", "password": "ggg"})
        status_code = response.status_code
        self.assertEqual(status_code, 302)
        self.assertTrue('Location' in response)
        self.assertIn('/', response['Location'])

    def test_user_register(self):
        user_client = Client()
        response = user_client.post('/user/register', {'username': 'somName', 'password': 'somePassword',
                                                       'email': 'someEmail@example.com'})
        status_code = response.status_code
        self.assertEqual(status_code, 302)

        created_user = User.objects.filter(username='somName').first()
        self.assertIsNotNone(created_user)

        login_response = user_client.login(username='somName', password='somePassword')
        self.assertTrue(login_response)
        self.assertTrue('Location' in response)
        self.assertIn('/user/login', response['Location'])


