class TimeFormat(object):
    """
    by: liaochuntao
    """
    def __init__(self, time: str):
        self.month_dic = {'01': 'January',
                          '02': 'January',
                          '03': 'Mar',
                          '04': 'April',
                          '05': 'May',
                          '06': 'June',
                          '07': 'July',
                          '08': 'August',
                          '09': 'September',
                          '10': 'October',
                          '11': 'November',
                          '12': 'December'}
        self.hr_type = {'AM': ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'],
                        'PM': ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']}
        self.hr_pm_change = {'12': '12', '13': '01', '14': '02',
                             '15': '03', '16': '04', '17': '05',
                             '18': '06', '19': '07', '20': '08',
                             '21': '09', '22': '10', '23': '11'}
        self.am_pm = ['AM', 'PM']
        self.time = str(time)
        self.final_time_str = ''

    def time_str_analyze(self):

        def chose_type(tmp):
            if tmp in self.hr_type['AM']:
                return self.time[11: 16] + 'AM'
            if tmp in self.hr_type['PM']:
                return self.hr_pm_change[self.time[11: 13]] + ':' + self.time[15: 17] + 'PM'

        month = self.month_dic[self.time[5: 7]]
        day = self.time[8: 10]
        time_type = chose_type(self.time[11: 13])
        self.final_time_str = month + ' ' + day + ' ' + time_type
        return self.final_time_str


if __name__ == '__main__':
    TimeFormat(time='2018-04-12 09:00:00').time_str_analyze()



