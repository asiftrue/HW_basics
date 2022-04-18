import re
import time


class MyErr(Exception):
    pass


class Date:
    def __init__(self, date: str):
        self.date = date

    @staticmethod
    def validate(date):
        try:
            day = date[0:2]
            if int(day) > 31:
                raise MyErr('Error: Day should be less than 31.')
        except MyErr as err:
            print(err)
        try:
            time.strptime(date, '%d-%m-%Y')
        except ValueError as err:
            print(err)

    @classmethod
    def extract(cls, date):
        pattern = re.compile(r'(?P<day>\d{1,2})[-](?P<month>\d{2})[-](?P<year>\d{4})')
        gr = re.search(pattern, date)
        dd = gr.group(1)
        mm = gr.group(2)
        yyyy = gr.group(3)
        return int(dd), int(mm), int(yyyy)


date_1 = Date('10-12-2022')
print(date_1.extract('10-12-2022'))
Date.validate('60-12-2022')
date_1.validate('40-13-2022')
