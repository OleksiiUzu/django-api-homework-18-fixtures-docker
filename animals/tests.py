from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from animals.models import Animal, Schedule, Sex
from animals.schedule_calculations import time_to_visit
import datetime


class TestSchedule(TestCase):

    def setUp(self):
        self.animal_id = 1
        self.user = Client()
        self.request_post = 2
        self.animal_id = 1

        self.request_post = 2
        self.reserve_dates = [[datetime.datetime(year=2023, month=3, day=12, hour=12, minute=0).replace(tzinfo=None),
                               datetime.datetime(year=2023, month=3, day=12, hour=13, minute=0).replace(tzinfo=None)]]

        self.times = time_to_visit(self.request_post, self.reserve_dates)
        self.hours = self.request_post
        self.animal_sex = Sex.objects.create(id=2, name='Female')
        self.animal = Animal.objects.create(name='Jenifer Lopez',
                                            animal_type='Dog',
                                            age=3,
                                            breed='pug',
                                            availability=1,
                                            description='',
                                            healthy=1,
                                            sex_id=2)

    def test_animal(self):
        response = self.user.get(f'/animals/animal_id={self.animal_id}')
        self.assertEqual(200, response.status_code)

    def test_schedule(self):
        data = {'times': self.times,
                'reserve_dates': self.reserve_dates,
                'hours': self.hours,
                'val': 1}
        response = self.user.post(f'/animals/animal_id={self.animal_id}/schedule', data)
        self.assertEqual(200, response.status_code)

    def test_time_list(self):
        data = {
            'time': '12:00',
            'hour': '2'
        }
        user = User.objects.create_user(username='test', password='test')
        self.user.login(username='test', password='test')
        response = self.user.post(f'/animals/animal_id={self.animal_id}/schedule/reserve', data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f'/animals/animal_id={self.animal_id}/schedule')

        schedule_entry = Schedule.objects.last()
        self.assertIsNotNone(schedule_entry)
        self.assertEqual(schedule_entry.user, user.id)
        self.assertEqual(schedule_entry.animal_id, self.animal_id)

        expected_start_time = datetime.datetime.now().replace(
            hour=12, minute=0, second=0, microsecond=0, tzinfo=None)
        expected_end_time = expected_start_time + datetime.timedelta(hours=2)
        self.assertEqual(schedule_entry.start_time.replace(tzinfo=None), expected_start_time)
        self.assertEqual(schedule_entry.end_time.replace(tzinfo=None), expected_end_time)
        self.assertEqual(Schedule.objects.count(), 1)
