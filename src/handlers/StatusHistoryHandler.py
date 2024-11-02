from src.service_classes.TimeDeltaCalculator import TimeDeltaCalculator


class StatusHistoryHandler:

    @classmethod
    def get_issue_status_history(cls, issue_status_history: list, time_format: str) -> list:
        status_history = []
        for changes in issue_status_history:
            for item in changes['items']:
                if item['field'] == 'status':
                    item['date'] = changes['created']
                    status_history.append(item)
        for i in range(len(status_history) - 1):
            delta = TimeDeltaCalculator.calculate_delta(status_history[i]['date'],
                                                        status_history[i + 1]['date'],
                                                        time_format)
            status_history[i]['status_duration'] = delta
        result = []
        for i in status_history[0:-1]:
            entry = {'status': i['toString'], 'duration': i['status_duration'], 'changed': i['date']}
            result.append(entry)
        return result

    @classmethod
    def _get_status_duration(cls, issue_status_history: list, status: str) -> [list, None]:
        result = []
        print('Issue status history: \n', issue_status_history)
        for entry in issue_status_history:
            print('Checking entry in history with status ', status)
            if entry['status'] == status:
                print('Found! ', entry)
                result.append(entry)
        if len(result) == 0:
            return None
        else:
            return result

    @classmethod
    def get_duration_between_statuses(cls, issue_status_history: list,
                                      start_status: str,
                                      end_status: str,
                                      time_format: str) -> [dict, None]:
        print('Starting processing history entry: \n'
              '_______________________________________________')
        dates = {}
        result = {}
        for entry in issue_status_history:
            if entry['status'] == start_status:
                print(entry)
                dates['first_date'] = entry['changed']
                print(dates)
                break
        if 'first_date' not in dates:
            print(f'There is no entry with start status {start_status}!')
            return

        issue_status_history.reverse()
        for entry in issue_status_history:
            if entry['status'] == end_status:
                print(entry)
                dates['second_date'] = entry['changed']
                print(dates)
                break
        if 'second_date' not in dates:
            print(f'There is no entry with end status {start_status}!')
            return

        delta = TimeDeltaCalculator.calculate_delta(dates['first_date'],
                                                    dates['second_date'],
                                                    time_format)

        result['delta'] = delta
        result['first_date'] = dates['first_date']
        result['second_date'] = dates['second_date']
        print('End processing \n'
              '_______________________________________________')
        return result
