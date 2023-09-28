from datetime import timedelta
import datetime


class TimeRange:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def intersects(self, other_ranges):
        for other_range in other_ranges:

            start_time_other, end_time_other = other_range
            if (
                    (self.start_time <= start_time_other <= self.end_time) or
                    (self.start_time <= end_time_other <= self.end_time) or
                    (start_time_other <= self.start_time <= end_time_other)
            ):
                return True

        return False


def time_to_visit(duration, booked_times):
    opening_time = datetime.datetime(2023, 8, 1, 8, 0)
    closing_time = datetime.datetime(2023, 8, 1, 18, 0)

    main = []
    current_time = opening_time

    modified_booked_times = []
    if booked_times:
        for i in booked_times:
            start_time = i[0] + timedelta(minutes=1)
            end_time = i[1] - timedelta(minutes=1)
            modified_booked_times.append([start_time, end_time])
    while current_time <= closing_time:
        current_closed_time = current_time + timedelta(hours=duration)
        range1 = TimeRange(current_time, current_closed_time)

        if not range1.intersects(modified_booked_times):
            main.append(f'{current_time.hour}:{current_time.minute}')

        current_time += timedelta(minutes=15)

        if current_closed_time >= closing_time:
            break

    return main


x = [
    [datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0)],
    [datetime.datetime(2023, 8, 1, 9, 0), datetime.datetime(2023, 8, 1, 10, 0)],
    [datetime.datetime(2023, 8, 1, 10, 0), datetime.datetime(2023, 8, 1, 11, 0)],
    [datetime.datetime(2023, 8, 1, 11, 0), datetime.datetime(2023, 8, 1, 12, 0)],
    [datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 13, 0)],
    [datetime.datetime(2023, 8, 1, 13, 0), datetime.datetime(2023, 8, 1, 14, 0)],
    [datetime.datetime(2023, 8, 1, 14, 0), datetime.datetime(2023, 8, 1, 15, 0)],
    [datetime.datetime(2023, 8, 1, 15, 0), datetime.datetime(2023, 8, 1, 16, 0)],
    [datetime.datetime(2023, 8, 1, 16, 0), datetime.datetime(2023, 8, 1, 17, 0)],

    ]
y = 1

print(time_to_visit(y, x))