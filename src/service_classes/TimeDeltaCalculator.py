from datetime import datetime


class TimeDeltaCalculator:
    JIRA_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'

    @classmethod
    def calculate_delta(cls, first_date: str, second_date: str, time_format='days'):
        current_status_datetime = datetime.strptime(first_date, cls.JIRA_DATE_FORMAT)
        next_status_datetime = datetime.strptime(second_date, cls.JIRA_DATE_FORMAT)
        delta = (next_status_datetime.timestamp() - current_status_datetime.timestamp())
        if time_format == 'days':
            # Если разница меньше 12 часов - считаем разницу равной 0
            if delta < 43200:
                return 0
            else:
                delta = delta / 3600 / 24
                return round(delta, 2)
        elif time_format == 'hours':
            delta = delta / 3600
            return round(delta, 2)
