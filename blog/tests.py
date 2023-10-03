from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from animals.models import Animal, Sex
from blog.models import Feedback

class Test_Blogs(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.animal_sex = Sex.objects.create(id=1, name='male')
        self.animal_data = Animal.objects.create(name='Chupakabra', animal_type='Some Evil Monster', age=1235341253246, availability=0, healthy=1, sex_id=1)

    def test_feedback_post(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'Some test title',
            'text': 'Some test text',
            'media': 'Some test media',
            'animal_type': self.animal_data.id,
        }

        response = self.client.post('/blog/feedback', data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Feedback.objects.count(), 1)

    def test_feedback_get(self):
        response = self.client.get('/blog/feedback')
        self.assertEqual(response.status_code, 200)


