from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from animals.models import Animal, Sex
from blog.models import Feedback


class Test_Blogs(TestCase):
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()
        self.user = self.client.login(username='ggg', password='ggg')
        self.animal_data = Animal.objects.first()

    def test_feedback_post(self):
        data = {
            'title': 'Some test title',
            'text': 'Some test text',
            'media': 'Some test media',
            'animal_type': self.animal_data.id,
        }

        response = self.client.post('/blog/feedback', data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Feedback.objects.count(), 9)

    def test_feedback_get(self):
        response = self.client.get('/blog/feedback')
        self.assertEqual(response.status_code, 200)


