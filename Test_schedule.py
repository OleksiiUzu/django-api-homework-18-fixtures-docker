import datetime
import unittest
from animals.schedule_calculations import time_to_visit


class TestSchedule(unittest.TestCase):
    def test_schedule_1(self):
        x = [
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 13, 0)],
        ]
        y = 1

        result = time_to_visit(y, x)
        self.assertEqual(result, ['9:0', '9:15', '9:30', '9:45', '10:0', '10:15', '10:30', '10:45', '11:0', '13:0', '13:15', '13:30', '13:45', '14:0', '14:15', '14:30', '14:45', '15:0', '15:15', '15:30', '15:45', '16:0', '16:15', '16:30', '16:45', '17:0'])

    def test_schedule_2(self):
        x = [
            [datetime.datetime(2023, 8, 1, 9, 0), datetime.datetime(2023, 8, 1, 12, 0)],
            [datetime.datetime(2023, 8, 1, 14, 0), datetime.datetime(2023, 8, 1, 18, 0)],
        ]
        y = 2

        result = time_to_visit(y, x)
        self.assertEqual(result, ['12:0'])

    def test_schedule_3(self):
        x = [
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 14, 0)],
        ]
        y = 2

        result = time_to_visit(y, x)
        self.assertEqual(result, ['9:0', '9:15', '9:30', '9:45', '10:0', '14:0', '14:15', '14:30', '14:45', '15:0', '15:15', '15:30', '15:45', '16:0'])

    def test_schedule_4(self):
        x = [
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 14, 0)],
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            ]
        y = 2

        result = time_to_visit(y, x)
        self.assertEqual(result, ['9:0', '9:15', '9:30', '9:45', '10:0', '14:0', '14:15', '14:30', '14:45', '15:0', '15:15', '15:30', '15:45', '16:0'])

    def test_schedule_5(self):
        x = [
            ]
        y = 1

        result = time_to_visit(y, x)
        self.assertEqual(result, ['8:0', '8:15', '8:30', '8:45', '9:0', '9:15', '9:30', '9:45', '10:0', '10:15', '10:30', '10:45', '11:0', '11:15', '11:30', '11:45', '12:0', '12:15', '12:30', '12:45', '13:0', '13:15', '13:30', '13:45', '14:0', '14:15', '14:30', '14:45', '15:0', '15:15', '15:30', '15:45', '16:0', '16:15', '16:30', '16:45', '17:0'])

    def test_schedule_6(self):
        x = [
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 18, 0)],
            ]
        y = 1

        result = time_to_visit(y, x)
        self.assertEqual(result, [])

    def test_schedule_7(self):
        x = [
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 12, 0)],
            ]
        y = 12

        result = time_to_visit(y, x)
        self.assertEqual(result, [])

    def test_schedule_8(self):
        x = [
            ]
        y = 9

        result = time_to_visit(y, x)
        self.assertEqual(result, ['8:0', '8:15', '8:30', '8:45', '9:0'])

    def test_schedule_9(self):
        x = [
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 14, 0)],
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            [datetime.datetime(2023, 8, 1, 15, 0), datetime.datetime(2023, 8, 1, 16, 0)],
            ]
        y = 1

        result = time_to_visit(y, x)
        self.assertEqual(result, ['9:0', '9:15', '9:30', '9:45', '10:0', '10:15', '10:30', '10:45', '11:0', '14:0', '16:0', '16:15', '16:30', '16:45', '17:0'])

    def test_schedule_10(self):
        x = [
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 14, 0)],
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            [datetime.datetime(2023, 8, 1, 15, 0), datetime.datetime(2023, 8, 1, 16, 0)],
            ]
        y = 2

        result = time_to_visit(y, x)
        self.assertEqual(result, ['9:0', '9:15', '9:30', '9:45', '10:0', '16:0'])

    def test_schedule_11(self):
        x = [
            [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
            [datetime.datetime(2023, 8, 1, 16, 0), datetime.datetime(2023, 8, 1, 17, 0)],
            [datetime.datetime(2023, 8, 1, 10, 0), datetime.datetime(2023, 8, 1, 11, 0)],
            [datetime.datetime(2023, 8, 1, 11, 0), datetime.datetime(2023, 8, 1, 12, 0)],
            [datetime.datetime(2023, 8, 1, 9, 0), datetime.datetime(2023, 8, 1, 10, 0)],
            [datetime.datetime(2023, 8, 1, 13, 0), datetime.datetime(2023, 8, 1, 14, 0)],
            [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 13, 0)],
            [datetime.datetime(2023, 8, 1, 15, 0), datetime.datetime(2023, 8, 1, 16, 0)],
            [datetime.datetime(2023, 8, 1, 14, 0), datetime.datetime(2023, 8, 1, 15, 0)],
            ]
        y = 1

        result = time_to_visit(y, x)
        self.assertEqual(result, ['17:0'])
